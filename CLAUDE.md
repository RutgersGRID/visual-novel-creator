# Streamlit Template Project Commands and Style Guide

## Commands
- **Run app**: `streamlit run src/streamlit_template/app.py`
- **Tests**: `pytest src/tests/ --cov=src/streamlit_template`
- **Single test**: `pytest src/tests/test_file.py::test_function -v`
- **Lint**: `pre-commit run --all-files`
- **Package management**: `uv venv`, `uv sync`, `uv add package_name`

## Code Style
- **Formatting**: Black with default settings
- **Linting**: Ruff for static analysis and error checking
- **Type Annotations**: Required for all functions (parameters and return values)
- **Docstrings**: Google-style with Args/Returns sections
- **Imports**: Sort in order: standard lib, third-party, local packages
- **Error Handling**: Use explicit try/except blocks with specific exceptions
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Commit Messages**: Use conventional commits (feat, fix, docs, style, refactor)
