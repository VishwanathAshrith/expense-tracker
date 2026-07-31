import json
import uuid
from datetime import date as Date
from pathlib import Path

from src.models import Expense
from src.schemas import ExpenseCreate

STORAGE_FILE = Path("expenses.json")


def _read_expenses() -> list[Expense]:
    if not STORAGE_FILE.exists() or STORAGE_FILE.stat().st_size == 0:
        return []
    try:
        with open(STORAGE_FILE, "r") as f:
            raw = json.load(f)
            return [Expense(**item) for item in raw]
    except (json.JSONDecodeError, KeyError):
        return []


def _write_expenses(expenses: list[Expense]) -> None:
    with open(STORAGE_FILE, "w") as f:
        json.dump(
            [expense.model_dump(mode="json") for expense in expenses],
            f,
            indent=2,
        )


def get_all_expenses() -> list[Expense]:
    return _read_expenses()


def get_expenses_by_category(category: str) -> list[Expense]:
    expenses = _read_expenses()
    return [e for e in expenses if e.category.lower() == category.lower()]


def add_expense(data: ExpenseCreate) -> Expense:
    expenses = _read_expenses()
    new_expense = Expense(
        id=str(uuid.uuid4()),
        title=data.title,
        amount=data.amount,
        category=data.category,
        date=data.date,
    )
    expenses.append(new_expense)
    _write_expenses(expenses)
    return new_expense


def delete_expense(expense_id: str) -> Expense | None:
    expenses = _read_expenses()
    match = next((e for e in expenses if e.id == expense_id), None)
    if match is None:
        return None
    remaining = [e for e in expenses if e.id != expense_id]
    _write_expenses(remaining)
    return match


def calculate_total(expenses: list[Expense]) -> float:
    return round(sum(e.amount for e in expenses), 2)