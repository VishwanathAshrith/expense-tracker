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