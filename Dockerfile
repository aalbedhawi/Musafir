FROM python:3.13-slim

WORKDIR /app
COPY . /app
RUN python -m pip install -r requirements.txt
