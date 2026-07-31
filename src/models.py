from datetime import date

from pydantic import BaseModel


class Expense(BaseModel):
    id: str
    title: str
    amount: float
    category: str
    date: date