import pytest
from fastapi.testclient import TestClient

from src.main import app
from src import storage

client = TestClient(app)

VALID_EXPENSE = {
    "title": "Lunch",
    "amount": 12.50,
    "category": "Food",
    "date": "2026-07-31",
}


@pytest.fixture(autouse=True)
def reset_storage(tmp_path, monkeypatch):
    test_file = tmp_path / "expenses.json"
    test_file.write_text("[]")
    monkeypatch.setattr(storage, "STORAGE_FILE", test_file)


# ─── POST /expenses ───────────────────────────────────────────────────────────

def test_create_expense_returns_201():
    response = client.post("/expenses", json=VALID_EXPENSE)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Lunch"
    assert data["amount"] == 12.50
    assert data["category"] == "Food"
    assert "id" in data


def test_create_expense_missing_title_returns_422():
    payload = {**VALID_EXPENSE, "title": ""}
    response = client.post("/expenses", json=payload)
    assert response.status_code == 422


def test_create_expense_negative_amount_returns_422():
    payload = {**VALID_EXPENSE, "amount": -10}
    response = client.post("/expenses", json=payload)
    assert response.status_code == 422


def test_create_expense_invalid_date_returns_422():
    payload = {**VALID_EXPENSE, "date": "not-a-date"}
    response = client.post("/expenses", json=payload)
    assert response.status_code == 422


# ─── GET /expenses ────────────────────────────────────────────────────────────

def test_get_expenses_empty_list():
    response = client.get("/expenses")
    assert response.status_code == 200
    assert response.json() == []


def test_get_expenses_returns_created_expense():
    client.post("/expenses", json=VALID_EXPENSE)
    response = client.get("/expenses")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_expenses_filter_by_category():
    client.post("/expenses", json=VALID_EXPENSE)
    client.post("/expenses", json={**VALID_EXPENSE, "category": "Transport"})
    response = client.get("/expenses?category=Food")
    assert response.status_code == 200
    results = response.json()
    assert len(results) == 1
    assert results[0]["category"] == "Food"


def test_get_expenses_filter_case_insensitive():
    client.post("/expenses", json=VALID_EXPENSE)
    response = client.get("/expenses?category=food")
    assert response.status_code == 200
    assert len(response.json()) == 1


# ─── GET /expenses/total ──────────────────────────────────────────────────────

def test_get_total_empty_list():
    response = client.get("/expenses/total")
    assert response.status_code == 200
    assert response.json()["total"] == 0.0


def test_get_total_with_expenses():
    client.post("/expenses", json=VALID_EXPENSE)
    client.post("/expenses", json={**VALID_EXPENSE, "amount": 7.50})
    response = client.get("/expenses/total")
    assert response.status_code == 200
    assert response.json()["total"] == 20.0


def test_get_total_by_category():
    client.post("/expenses", json=VALID_EXPENSE)
    client.post("/expenses", json={**VALID_EXPENSE, "category": "Transport", "amount": 5.0})
    response = client.get("/expenses/total?category=Food")
    assert response.status_code == 200
    assert response.json()["total"] == 12.50


def test_get_total_nonexistent_category_returns_404():
    response = client.get("/expenses/total?category=NonExistent")
    assert response.status_code == 404


# ─── DELETE /expenses/{id} ────────────────────────────────────────────────────

def test_delete_expense_returns_200():
    created = client.post("/expenses", json=VALID_EXPENSE).json()
    response = client.delete(f"/expenses/{created['id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Expense deleted successfully"


def test_delete_expense_removes_from_list():
    created = client.post("/expenses", json=VALID_EXPENSE).json()
    client.delete(f"/expenses/{created['id']}")
    response = client.get("/expenses")
    assert response.json() == []


def test_delete_nonexistent_expense_returns_404():
    response = client.delete("/expenses/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404