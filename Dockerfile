FROM python:3.8-slim-buster

WORKDIR /src

COPY ./src/requirements.txt .
RUN pip install -r requirements.txt
