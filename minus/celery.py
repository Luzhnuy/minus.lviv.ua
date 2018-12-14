from __future__ import absolute_import
import os
from celery.schedules import crontab
from celery import Celery
from django.conf import settings
import datetime

# устанавливаем settings модуль для приложения celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minus.settings')

# создаем celery-приложение
app = Celery()

# используем установки django-проекта в celery-приложении
app.config_from_object('django.conf:settings')

# автоопределение задач из django-проекта
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



app.conf.beat_schedule = {
    'send_new_minuses': {
        'task': 'minusstore.tasks.minus_send_new',
        'schedule': crontab(day_of_week=1),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnightd
    },
}
app.conf.timezone = 'UTC'
