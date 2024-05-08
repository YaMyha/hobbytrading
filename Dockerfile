FROM python:3.12

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /fastapi_app/docker/*.sh

alembic upgrade head

WORKDIR src

gunicorn api:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000