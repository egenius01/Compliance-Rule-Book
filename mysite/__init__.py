from __future__ import absolute_import, unicode_literals
#this will make sure the app is always imported when
# Django starts so that shared_task will use the app.
from .celery import app as celery_app

__all__ = ('celery_app',)
