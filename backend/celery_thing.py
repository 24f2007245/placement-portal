from celery import Celery, Task
from celery.schedules import crontab

from app import create_app 

flask_app = create_app()

celery_app = Celery(
    broker='redis://localhost:6379',
    backend='redis://localhost:6379',
    include=['mail_server']
)

class FlaskTask(Task):
    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)

celery_app.Task = FlaskTask   


celery_app.conf.beat_schedule = {
    'monthly-user-report': {
        'task': 'mail_server.send_monthly_report',  
        'schedule': crontab(hour=0, minute=0, day_of_month=1),#hour=0, minute=0, day_of_month=1
    },
    'daily-reminder':{
        'task': 'mail_server.send_daily_reminder',
        'schedule': crontab(1),         #minute='*/2' | hour=10, minute=0
    },
}   
      