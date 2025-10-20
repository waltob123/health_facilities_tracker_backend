# Contributing to Health Facilities Tracker

Thank you for considering contributing to Health Facilities Tracker! We appreciate your support and are excited to collaborate with you.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
   - [Reporting Bugs](#reporting-bugs)
   - [Suggesting Features](#suggesting-features)
   - [Submitting Changes](#submitting-changes)
3. [Development Setup](#development-setup)
4. [Style Guidelines](#style-guidelines)
5. [Git Commit Guidelines](#git-commit-guidelines)
6. [License](#license)

## Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code.

## How to Contribute

### Reporting Bugs
 
If you find a bug, please report it by opening an issue on our [GitHub Issues page](https://github.com/ghsentnoc/health_facilities_tracker_backend/issues). Provide as much detail as possible, including steps to reproduce the issue, the version of the project you are using, and any relevant logs or screenshots.

### Suggesting Features

We welcome suggestions for new features! Please open an issue on our [GitHub Issues page](https://github.com/ghsentnoc/health_facilities_tracker_backend/issues) and describe the feature you would like to see, why you need it, and how it should work.

### Submitting Changes

1. Clone the repository if you haven't else pull from main (`git pull origin main`).
2. Create a new branch (`git checkout -b <type>/your-feature-name`). (example of type 'feature', 'fix', 'docs', 'style', 'refactor', 'perf', 'test', 'chore')
3. Make your changes.
4. Commit your changes.
    - `git commit -m 'type(scope): subject'` for small changes.
    - For larger changes, please use a more descriptive commit message following the [Git Commit Guidelines](#git-commit-guidelines).
5. Push to the branch (`git push -u origin <feature_branch>`).
6. Open a pull request from your <feature_branch> to trunk.

Please ensure your code follows the project's style guidelines and includes tests where applicable.

## Development Setup

To set up the development environment:

1. Clone the repository: `git clone https://<your-token>@github.com/ghsentnoc/health_facilities_tracker_backend`
2. Change to the project directory: `cd health_facilities_tracker_backend`
3. Create a virtual environment: `python -m venv ./.venv`
4. Activate the virtual environment:
   - On Windows: `.\.venv\Scripts\activate`
   - On Unix or macOS or Linux : `source ./.venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Install development dependencies: `pip install -r requirements-dev.txt`
7. Set up environment variables as needed (refer to `.env.example` for guidance).

## Running the Application with a Docker

To run the application using Docker, ensure you have Docker installed and run the following command:

```
./run_app_with_docker.sh
```

## Running the Application with Uvicorn

To run the application locally using Uvicorn, execute the following command:

```bash
./run_app_with_uvicorn.sh
```

## Style Guidelines

We follow the PEP 8 style guide for Python code. Please ensure your code adheres to these guidelines:

- **Indentation**: Use 4 spaces per indentation level.
- **Line Length**: Limit all lines to a maximum of 79 characters.
- **Imports**:
  - Import standard libraries first, followed by third-party libraries, and then local imports.
  - Use absolute imports rather than relative imports.
- **Naming Conventions**:
  - Use `snake_case` for variable and function names.
  - Use `CamelCase` for class names.
  - Use `UPPER_CASE` for constants.
- **Docstrings**:
  - Write docstrings for all public modules, functions, classes, and methods.
  - Use triple double quotes (`"""`).
- **Spaces**:
  - Use a single space after commas, colons, and semicolons.
  - Use a single space around operators (assignment `=`, arithmetic `+`, etc.), except for when used in arguments.
  - Do not use spaces around the `=` sign when used to indicate a keyword argument or a default parameter value.

## Check your code against these guidelines before submitting.

Run the following command to check your code:

```bash
./run_lint_tests.sh
```

## Git Commit Guidelines

We follow the conventional commits specification for our git commit messages. Please ensure your commit messages adhere to these guidelines:

### Format

Each commit message should include a type, an optional scope, and a subject: 

```text
type(scope): subject

description here
- You list the changes here.
```
Example:
### Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semicolons, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools and libraries such as documentation generation

### Scope

The scope should be the name of the module affected (as perceived by the person reading the changelog generated from commit messages).

Example of scope: `models` `service` `routes` `schemas` etc.

### Subject

The subject contains a succinct description of the change:

- Use the imperative, present tense: "change" not "changed" nor "changes"
- Do not capitalize the first letter
- Do not end the subject with a period


## License

MIT License

Copyright (c) [2025]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
