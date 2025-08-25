FROM python:3.13.3-alpine3.21 AS base

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

FROM base AS dev

COPY . .

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]