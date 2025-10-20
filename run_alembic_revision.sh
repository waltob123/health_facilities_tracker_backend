#!/usr/bin/env bash

# This script is used to run alembic revision with autogenerate

alembic revision --autogenerate -m "$1"
