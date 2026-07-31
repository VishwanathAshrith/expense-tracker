from fastapi import FastAPI

from src.routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A REST API to add, view, filter, and delete personal expenses.",
    version="1.0.0",
)

app.include_router(router)


@app.get("/", tags=["Health"])
def root():
    return {"message": "Smart Expense Tracker API is running!"}


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}