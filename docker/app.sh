#!/bin/bash

alembic upgrade head

cd src

gunicorn api:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
