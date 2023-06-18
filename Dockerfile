FROM python:3.8-slim-buster

WORKDIR /app

COPY ./src/requirements.txt .
RUN pip install -r requirements.txt
RUN touch __init__.py
