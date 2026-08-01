# Smart Expense Tracker API

A REST API for managing personal expenses, built with Python and FastAPI.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate category-wise totals
- Delete an expense by ID
- Input validation with meaningful error messages
- Persistent JSON file storage
- Interactive API documentation via Swagger UI

## Project Structure
expense-tracker/
├── src/
│ ├── init.py
│ ├── main.py # App entry point
│ ├── routes.py # API endpoint definitions
│ ├── storage.py # JSON file read/write logic
│ ├── models.py # Expense response model
│ └── schemas.py # Request validation schema
├── tests/
│ ├── init.py
│ └── test_api.py # pytest test suite
├── expenses.json # Local data storage
├── requirements.txt
└── README.md

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Server

```bash
uvicorn src.main:app --reload
```

API will be available at `http://127.0.0.1:8000`

Swagger UI at `http://127.0.0.1:8000/docs`

## Running Tests

```bash
pytest tests/ -v
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | List all expenses |
| GET | `/expenses?category=Food` | Filter by category |
| GET | `/expenses/total` | Get total of all expenses |
| GET | `/expenses/total?category=Food` | Get total for a category |
| DELETE | `/expenses/{id}` | Delete an expense by ID |

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/expenses \
  -H "Content-Type: application/json" \
  -d '{"title": "Lunch", "amount": 12.50, "category": "Food", "date": "2026-07-31"}'
```

## Example Response

```json
{
  "id": "9bcb3883-ce9c-451b-8115-f9f485193d73",
  "title": "Lunch",
  "amount": 12.5,
  "category": "Food",
  "date": "2026-07-31"
}
```

## Technologies

- Python 3.12
- FastAPI
- Pydantic v2
- Uvicorn
- Pytest
- httpx

## Bonus

Interactive OpenAPI/Swagger documentation available at `/docs` — generated automatically by FastAPI.