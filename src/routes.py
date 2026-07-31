from fastapi import APIRouter, HTTPException, Query

from src.models import Expense
from src.schemas import ExpenseCreate
from src import storage

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("", status_code=201)
def create_expense(data: ExpenseCreate) -> Expense:
    return storage.add_expense(data)


@router.get("")
def list_expenses(category: str | None = Query(default=None)) -> list[Expense]:
    if category is not None:
        return storage.get_expenses_by_category(category)
    return storage.get_all_expenses()


@router.get("/total")
def get_total(category: str | None = Query(default=None)) -> dict:
    if category is not None:
        expenses = storage.get_expenses_by_category(category)
        if not expenses:
            raise HTTPException(
                status_code=404,
                detail=f"No expenses found for category '{category}'",
            )
        return {"category": category, "total": storage.calculate_total(expenses)}
    expenses = storage.get_all_expenses()
    return {"total": storage.calculate_total(expenses)}


@router.delete("/{expense_id}", status_code=200)
def delete_expense(expense_id: str) -> dict:
    deleted = storage.delete_expense(expense_id)
    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail=f"Expense with id '{expense_id}' not found",
        )
    return {"message": "Expense deleted successfully", "expense": deleted}