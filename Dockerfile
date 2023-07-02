FROM python:3.8-slim-buster

ENV PYTHONPATH="$PYTHONPATH:/app"

WORKDIR /app

COPY ./src/requirements.txt .
RUN pip install -r requirements.txt
