# Math Operations Example

This repository provides basic math operations with automated tests and CI integration.

## Python Functions
- Addition: `add(a, b)`
- Subtraction: `subtract(a, b)`

## Usage
```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 3))   # Output: 2
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

## CI Workflow
- The workflow is defined in `.github/workflows/ci.yml`.
- Tests run automatically on push to the `Feature1` branch.

## Requirements
- Python 3.10+
- pytest
