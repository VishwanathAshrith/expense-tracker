# AI Notes

## Tools Used
- Claude (Anthropic) — primary tool throughout the project

## What was AI-generated

**Structure and architecture:**
The overall project layout, file separation (models, schemas, storage, routes), 
and the decision to use private helper functions like `_read_expenses` and 
`_write_expenses` were all suggested by Claude.

**src/models.py** — AI-generated entirely. Simple Pydantic model with five fields.

**src/schemas.py** — AI-generated structure. I debugged a real error:
Claude's first version used `Field(..., min_length=1)` with `...` as a positional 
argument, which caused a `PydanticUserError` in Pydantic v2.13. Claude also used 
`from datetime import date` which conflicted with the field named `date` on the 
same class. I worked through both errors and applied the fixes (`date as Date` alias, 
removing positional `...`).

**src/storage.py** — AI-generated. I verified the logic manually by running a 
direct Python test before building routes on top of it.

**src/routes.py** — AI-generated. I tested every endpoint through Swagger UI 
at `/docs` and confirmed correct status codes (201, 200, 404).

**src/main.py** — AI-generated. Minimal entry point.

**tests/test_api.py** — AI-generated structure and test cases. I ran the full 
suite and verified all 15 tests passed. The `monkeypatch` fixture approach for 
isolating tests from real storage was new to me — I understood it before accepting it.

## What I changed or rejected

- Rejected more complex patterns suggested early on (middleware, config files, 
  constants module) — they added complexity without adding marks for this scope.
- Debugged the Pydantic v2 `Field(...)` syntax issue myself rather than asking 
  AI to fix it blindly.
- Fixed the `date` type name conflict myself after reading the error message.
- Identified the missing `source venv/bin/activate` issue when packages weren't 
  found — AI didn't catch this, I did.

## What I personally contributed

- All terminal work, file creation, and debugging
- Reading and understanding every error before fixing it
- Manual testing of all 6 endpoints through Swagger UI
- Verifying case-insensitive category filtering worked correctly
- Caught several issues where AI output wasn't saved or applied correctly

## Honest summary

This project was heavily AI-assisted in terms of code generation. My contribution 
was in understanding, debugging, testing, and making judgment calls about what to 
include or reject. I did not copy-paste blindly — every file was read and every 
error was investigated before moving forward.