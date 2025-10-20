#!/usr/bin/env bash

# Load the environment variables from the .env file
source .env

echo "Project Environment: $PROJECT_ENV"

# Run the FastAPI uvicorn server
echo "Running the FastAPI server"
echo "==================================================="
uvicorn app.main:app --reload --host "$HOST" --port "$PORT"
