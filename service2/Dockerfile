# syntax=docker/dockerfile:1
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN mkdir /project2

WORKDIR /project2

COPY ./service2 .

RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8001"]