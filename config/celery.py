from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

import logging
logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'send-daily-likes-notification': {
        'task': 'recipe.tasks.send_daily_likes_notification',
        'schedule': crontab(hour=0, minute=0),  # Runs daily at midnight
    },
}


@app.task(bind=True)
def debug_task(self):
    logger.info(f'Request: {self.request!r}')

