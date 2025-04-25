import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
app = Celery('publish', broker_connection_retry=False,
             broker_connection_retry_on_startup=True, )
app.config_from_object('django.conf:settings')
broker_connection_retry = False

app.autodiscover_tasks()

# celery beat - выполнение задачи через определное количество минут 

# app.conf.beat_schedule = {
#     'send-report-every-single-minute': {
#         'task': 'здесь регистрируем таску которая будет выполнятся каждую минуту'
#         'schedule': crontab(), 
#     },
#    'send-report-every-minute': {
#       'task': 'myapp.tasks.send_report',
#       'schedule': crontab(),  # каждую минуту
#     },
#     'clear-temp-files-every-hour': {
#         'task': 'myapp.tasks.clear_temp_files',
#         'schedule': crontab(minute=0),  # каждый час в 00 минут
#     },
#     'daily-summary-at-midnight': {
#         'task': 'myapp.tasks.daily_summary',
#         'schedule': crontab(hour=0, minute=0),  # каждый день в полночь
#     },
#     'check-server-status-every-30-seconds': {
#         'task': 'myapp.tasks.check_server',
#         'schedule': timedelta(seconds=30),  # каждые 30 секунд
#     },
# }

# crontab() - по умолчанию выполняется каждую минуту 

# потом в еще одной консоли запускаем уже celery beat 
# celery -A publish beat