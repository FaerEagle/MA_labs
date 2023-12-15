FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN mkdir /consumer

WORKDIR /consumer

COPY ./consumer /consumer
COPY ./requirements.txt /consumer/requirements.txt

RUN pip install -r requirements.txt
RUN pip install pika

CMD ["python", "app/views.py"]