FROM python:3.8

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY ./app /app

ENTRYPOINT ["python", "-m", "app.main"]
