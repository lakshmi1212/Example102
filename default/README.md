# Math Operations Example

This repository demonstrates basic math operations (addition and subtraction) with production-ready tests and CI/CD integration.

## Usage

- Implemented functions: `add(a, b)` and `subtract(a, b)` in `src/math_operations.py`.
- Run tests using pytest:

```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI/CD Workflow

- Workflow file: `.github/workflows/ci.yml`
- Triggers on push to `Feature1` and pull request to `main`.
- Generates JUnit and HTML reports in `reports/`.

## Requirements

- Python 3.10
- pytest
- pytest-html

## Structure

- `src/`: Source code
- `tests/`: Test cases
- `default/`: Documentation and metadata
