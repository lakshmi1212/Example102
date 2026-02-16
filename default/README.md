# Example102: Math Operations

This repository provides simple math operations (addition and subtraction) with production-ready pytest test cases and a CI integration structure.

## Folder Structure

- `src/`: Source code for math operations
- `tests/`: Pytest test cases
- `default/requirements.txt`: Python dependencies
- `default/math.json`: Workflow metadata for CI/CD

## Usage

1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run tests:
   ```bash
   pytest tests/
   ```

## CI/CD Workflow
- The workflow file is located at `.github/workflows/ci.yml`.
- Tests are run automatically on push to `Feature1` branch or PR to `main`.

## Python Version
- Requires Python 3.10

---
See `default/math.json` for workflow and job metadata.
