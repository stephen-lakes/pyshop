import os
import celery

# Set the default django settings module for the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = celery.Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()