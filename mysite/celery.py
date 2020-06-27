from __future__ import absolute_import
import os
from celery import Celery
from django.core.mail import send_mail

from django.conf import settings

#set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery('mysite')

#Using a string here means the worker will not have to
#pickle the object when using windows.

# namespace='CELERY' means the worker doesnt havee to serialise the configuration
#keys  should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

#Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# @app.task(bind=True)
# def send():
#     send_mail('Celery Task Worked',
#               ' Just Posted a Rule Proof Kindly Authenticate',
#               'sender',
#               ['reciever'])
#     return None
#
# app.conf.beat_schedule = {
#     "see-you-in-ten-seconds-task": {
#         "task": "periodic.send",
#         "schedule": 10.0
#     }
# }

