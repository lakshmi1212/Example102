# Example102 Math Operations

This repository provides simple math operations (addition and subtraction) with production-ready code, tests, and CI integration.

## Usage

```
from src.math_operations import add, subtract

result1 = add(2, 3)        # 5
result2 = subtract(5, 2)   # 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests with:

```
pytest tests/
```

## CI Workflow

The repository is configured with a GitHub Actions workflow at `.github/workflows/ci.yml` for automated test execution and report generation.
