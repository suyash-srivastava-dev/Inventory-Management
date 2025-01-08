FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "ims.wsgi:application", "--bind", "0.0.0.0:8000"]