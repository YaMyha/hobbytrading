FROM python:3.12

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /fastapi_app/docker/*.sh
#WORKDIR src

#CMD gunicorn api:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000