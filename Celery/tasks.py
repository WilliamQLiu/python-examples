""" Testing out Celery """

from celery import Celery


### Configure Celery with Messaging Broker

#BROKER_URL = 'ampq://guest@localhost//'  # RabbitMQ
BROKER_URL = 'redis://localhost:6379/0'  # redis://password@hostname:port/db_number
app = Celery('tasks', broker=BROKER_URL)


@app.task
def add(x, y):
    return x + y

