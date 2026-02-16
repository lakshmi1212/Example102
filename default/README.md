# Example102 Math Operations

This repository implements basic math operations (addition, subtraction) and provides comprehensive pytest test cases.

## Usage

- Import functions from `src/math_operations.py`
- Run tests using pytest:

```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow

- Workflow file: `.github/workflows/ci.yml`
- Python version: 3.10
- Default branch: main
- Feature branch: Feature1

## Test Reports

- JUnit XML: `reports/report.xml`
- HTML: `reports/report.html`

## Requirements

See `default/requirements.txt` for dependencies.
