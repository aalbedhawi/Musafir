FROM python:3-slim

WORKDIR /app
COPY . /app
RUN python -m pip install -r requirements.txt

CMD ["pytest", "GameLogic/LoaderUnitTests.py"]
