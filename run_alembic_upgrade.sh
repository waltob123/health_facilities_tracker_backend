#!/usr/bin/env bash

# Run the alembic upgrade command with the provided argument or default to 'heads' to migrate the database
# Check if an argument is provided

if [[ $# -eq 0 ]]; then
    # No argument provided, default to 'heads'
    alembic upgrade heads
else
    # Use the provided argument
    alembic upgrade "$1"
fi
