from datetime import date as Date

from pydantic import BaseModel, Field, field_validator


class ExpenseCreate(BaseModel):
    title: str = Field(min_length=1, description="Title of the expense")
    amount: float = Field(gt=0, description="Amount must be greater than zero")
    category: str = Field(min_length=1, description="Category of the expense")
    date: Date = Field(description="Date in YYYY-MM-DD format")

    @field_validator("title", "category")
    @classmethod
    def must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Field cannot be empty or whitespace only")
        return value.strip()