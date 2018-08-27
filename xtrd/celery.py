import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xtrd.settings')
 
app = Celery('xtrd', broker='redis://redis:6379/0')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

"""
Execute every three hours:
midnight, 3am, 6am, 9am, noon, 3pm, 6pm, 9pm.
"""
app.conf.beat_schedule = {
    'parse-data-every-three-hours': {
        'task': 'api.tasks.parse_data',
        # 'schedule': crontab(minute=0, hour='*/3'),
        'schedule': crontab(),
    },
}
