""" Celery - distribute work across threads or machines
    Requires broker (e.g. redis), start with: $redis-server
    Run the worker by: $celery -A tasks worker --loglevel=info
"""

from celery import Celery
from celery.utils.log import get_task_logger  # Configure own logging


### Configure Celery with Messaging Broker
#BROKER_URL = 'ampq://guest@localhost//'  # RabbitMQ
BROKER_URL = 'redis://localhost:6379/0'  # Redis
#Note: redis://password@hostname:port/db_number
app = Celery('tasks', broker=BROKER_URL)

### Configure logger; a special logger is available as 'celery.task' which you
# can inherit to automatically get the task name and unique id as part of logs
logger = get_task_logger(__name__)  # Create common logger for all tasks

### Create tasks
# Usually use module name as a namespace (so names won't collide)
@app.task(name='tasks.add')
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x,y))
    return x + y


### Retry tasks
# 'retry' will re-execute a task, will send a new message to the same queue
# as originating task; can track progress of the task using the 'result' instance
@app.task(name='tasks.twitter')
def send_twitter_status(self, oauth, tweet):
    try:
        twitter = Twitter(oauth)
        twitter.update_status(tweet)
    except (Twitter.FailWhaleError, Twitter.LoginError) as exc:
        raise self.retry(exc=exc)


if __name__ == '__main__':
    app.worker_main()
