FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN mkdir -p /app
WORKDIR /app

RUN apt-get update && apt-get install libpq-dev python3-dev -y

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --deploy


ENV PYTHONPATH=/app