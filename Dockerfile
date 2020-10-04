FROM python:3.7-buster

WORKDIR /opt/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY users.json .
COPY app/ ./app
COPY tests/ ./tests

EXPOSE 5000

CMD ["python", "./app/app.py"]