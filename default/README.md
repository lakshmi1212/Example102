# Example102 Math Operations

## Overview

This repository implements basic math operations (addition, subtraction) in Python and provides comprehensive pytest-based test cases.

## Usage

- Source code is in `src/math_operations.py`.
- Tests are located in the `tests/` folder.

## Running Tests

1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run tests:
   ```bash
   pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
   ```

## CI/CD Workflow

- Workflow file: `.github/workflows/ci.yml`
- Tests run automatically on push to `Feature1` or pull request to `main`.
- Test reports are generated in the `reports/` directory and uploaded to S3.
