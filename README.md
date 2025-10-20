# Health Facilities Tracker

Health Facilities Tracker is a web platform that helps monitor and analyze healthcare services across facilities. It tracks facilities offering cervical cancer, and breast cancer care services, providing tools for data collection, auditing, and reporting. The goal is to drive data-informed decisions and improve health outcomes through better visibility and accountability in healthcare delivery.

## Table of Contents
- [Health Facilities Tracker](#health-facilities-tracker)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Database Setup](#database-setup)
  - [Running the Application with Docker](#running-the-application-with-a-docker)
  - [Running the Application with Uvicorn](#running-the-application-with-uvicorn)
  - [Deployment](#deployment)
  - [Project Structure](#project-structure)
  - [Testing](#testing)
    - [Testing Tips](#testing-tips)
  - [License](#license)



## Requirements

This project requires Python 3.10+ and the following dependencies:
- **FastAPI** for API development
- **SQLAlchemy** and **Alembic** for ORM and migrations
- **MySQL Connector** for MySQL database connections
- **Pydantic** for data validation
- **Uvicorn** as an ASGI server
- **Gunicorn** for production deployment
- **FastAPI-Mail** for email functionality

A full list of dependencies is provided in `requirements.txt`.

## Installation

1. Clone this repository:
   ```bash
   git clone https://{your-github-token}@github.com/ghsentnoc/health_facilities_tracker_backend
   cd health_facilities_tracker_backend
   ```

2. Creating virtual environment and activating it linux:
   ```bash
   python3 -m venv ./.venv
   source ./.venv/bin/activate 
   ```

3. Create a virtual environment and activate it on Windows:
   ```bash
   python -m venv .\.venv
   .\.venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

## Environment Variables

The project uses environment variables for sensitive settings like database credentials, email server details, etc.
Create a `.env` file in the root directory and define the following variables based on the variables in `.env.example` file
NB: Ensure your `.env` file is configured correctly to match the variables in `.env.example` file.

## Database Setup

Initialize the database schema and apply database migrations:

```bash
# Generate a new migration with a message
./run_alembic_revision.sh <message-goes-here>

# Apply the migrations to the database
./run_alembic_upgrade.sh
```

## Running the Application with a Docker

To run the application using Docker, ensure you have Docker installed and run the following command:

```bash
./run_app_with_docker.sh
```

## Running the Application with Uvicorn

To run the application locally using Uvicorn, execute the following command:

```bash
./run_app_with_uvicorn.sh
```


- Visit `http://127.0.0.1:8000/api/documentation` to view the interactive API documentation (Swagger UI).
- Visit `http://127.0.0.1:8000/api/redoc` to view the ReDoc API documentation.
- Visit `http://127.0.0.1:8000/api/<version>/documentation` to view the versioned API documentation (Swagger UI).
- Visit `http://127.0.0.1:8000/api/<version>/redoc` to view the versioned ReDoc API documentation.

## Deployment

For production, it is recommended to use Gunicorn with Uvicorn workers:

```bash
gunicorn main:app -k uvicorn.workers.UvicornWorker --bind $HOST:$PORT
```

## Project Structure

The project follows a modular structure, as shown below:

```plaintext
health_facilities_tracker_backend/
└── app
    ├── auth
    │   ├── dependencies
    │   ├── docs
    │   ├── factories
    │   ├── routes
    │   ├── schemas
    │   ├── services
    │   └── utils
    ├── core
    │   ├── config
    │   ├── dependencies
    │   ├── handlers
    │   └── utils
    ├── database
    ├── locations
    │   ├── dependencies
    │   ├── docs
    │   ├── factories
    │   ├── models
    │   ├── repositories
    │   ├── routes
    │   ├── schemas
    │   │   ├── request
    │   │   └── response
    │   ├── services
    │   └── utils
    └── users
        ├── dependencies
        ├── docs
        ├── factories
        ├── models
        ├── repositories
        ├── routes
        ├── schemas
        │   ├── request
        │   └── response
        ├── services
        └── utils
```

Each directory serves a specific purpose in maintaining a clean and organized codebase.


## Testing

To run tests, use `unittest`, `pytest` and `pytest-asyncio`:

```bash
pytest
```

### Testing Tips
- Ensure a test database is configured for running tests.
- Mock external dependencies (like email sending) to prevent unintended API calls.


## License

GHS License

Copyright (c) 2024 GHANA HEALTH SERVICE

GHANA HEALTH SERVICE LICENSE GOES HERE
.