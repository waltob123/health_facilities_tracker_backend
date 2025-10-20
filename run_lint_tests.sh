#!/usr/bin/env bash

# This script is used to run lint tests using flake8 and pylint
echo "========================================"
echo "Running lint tests..."
echo "========================================"
mypy .
ruff check .
black .
echo "Lint tests completed."
