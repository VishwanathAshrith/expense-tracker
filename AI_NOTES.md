# AI Notes

This file honestly documents how AI was used in this project.

## What AI suggested

- The overall project structure and file layout
- The Pydantic schema design including use of `field_validator`
- The storage layer pattern using `_read_expenses` and `_write_expenses` as private helpers
- The `monkeypatch` fixture approach for isolating tests from real storage
- The fix for the `date` field name conflict with Pydantic v2 (aliasing as `Date`)

## What I changed or questioned

- Debugged the `Field(...)` syntax issue with Pydantic v2.13 — AI's first suggestion used `...` as a positional argument which caused a `PydanticUserError`. Fixed by removing the positional argument.
- Identified that the venv was not activated when running commands — packages were not found until this was resolved.
- Ran all tests manually and verified each endpoint through Swagger UI.

## What I tested

- Verified all 6 endpoints through Swagger UI at `/docs`
- Ran the full pytest suite: 15/15 tests passed
- Manually tested category filtering with lowercase input to confirm case-insensitive matching

## What AI suggestions I rejected

- AI initially suggested more complex patterns that were unnecessary for this scope
- Kept the project deliberately simple — no middleware, no config files, no extra abstractions beyond what the assignment requires

## Honest reflection

The core structure was AI-guided. I typed, tested, and debugged every step myself. The errors I encountered (wrong venv, Pydantic version conflict, empty files from `touch`) were real mistakes I fixed by understanding what went wrong rather than blindly retrying.