FROM python:3.11

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install -r requirements.txt


WORKDIR /app
COPY . .

ENV FLASK_APP=app.py


ENTRYPOINT ["gunicorn", "--bind","0.0.0.0:5000", "app:app"]
