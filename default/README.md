# Example102 Math Operations

## Overview
This repository implements basic math operations (addition, subtraction) in Python, with automated tests and CI workflow integration.

## Usage

### Math Functions
- `add(a, b)`: Returns the sum of two numbers.
- `subtract(a, b)`: Returns the difference between two numbers.

### Running Tests
1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run all tests:
   ```bash
   pytest tests/
   ```

### CI Workflow
- The CI pipeline runs on every push to `Feature1` and pull request to `main`.
- Test reports are generated in JUnit and HTML formats.

## File Structure
```
src/
  math_operations.py
  __init__.py

tests/
  test_add.py
  test_subtract.py
  __init__.py

default/
  README.md
  requirements.txt
  math.json
```

## Requirements
- Python 3.10 or higher
- pytest
- pytest-html
