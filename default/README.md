# Example102: Math Operations

This repository provides basic math operations (addition and subtraction) with production-ready Python code and automated tests.

## Project Structure

- `src/` - Source code for math operations
- `tests/` - Pytest-based unit tests
- `default/requirements.txt` - Python dependencies
- `default/math.json` - CI/CD workflow metadata

## Usage

```python
from src.math_operations import add, subtract

print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
```

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run all tests:

```bash
pytest tests/
```

## CI/CD

Workflow file: `.github/workflows/ci.yml`

Workflow is triggered on push to `Feature1` and pull requests to `main`. See `default/math.json` for meta configuration.
