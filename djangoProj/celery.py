from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProj.settings')
app = Celery('djangoProj')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="task_save_latest_flickr_image",
    ignore_result=True
)
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    print("hello world")
    logger.info("Saved image from Flickr")