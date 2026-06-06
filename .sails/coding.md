# Sails Coding Protocol
- **Architecture**: Modular design. All logic in `src/`, entry points in root.
- **Python Specs**: Python 3.10+, absolute imports, strict `typing`.
- **Quality**: No wildcard imports, no `print()`. Use `logging`.
- **I/O**: Use `pathlib` for paths. All I/O must be in `try/except` blocks.
- **Validation**: Use `pydantic` or `dataclasses` for all data structures.
- **Audit**: Every code block must pass the "Sails Audit" (Type hints, error handling, security check).
