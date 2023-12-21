FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN mkdir /sender

WORKDIR /sender

COPY ./sender /sender
COPY ./requirements.txt /sender/requirements.txt

RUN pip install -r requirements.txt
RUN pip install pika

CMD ["python", "app/views.py"]
CMD ["python","manage.py","runserver", "0.0.0.0:8002"]