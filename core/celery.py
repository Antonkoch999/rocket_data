import os
from django.conf import settings
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'staff.tasks.payroll',
        'schedule': 7200,
    },
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
