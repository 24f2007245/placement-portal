from celery import Celery, Task
from celery.schedules import crontab

from app import create_app   # MUST be correct path

flask_app = create_app()

celery_app = Celery(
    'celery_thing',
    broker='redis://localhost:6379',
    backend='redis://localhost:6379',
    include=['mail_server']
)

class FlaskTask(Task):
    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)

celery_app.Task = FlaskTask

# class FlaskTask(Task):
#         def __call__(self, *args, **kwargs):
#             # from app import app
#             from app import create_app 
#             app = create_app()
#             with app.app_context():
                
#                 return self.run(*args, **kwargs)
            
# celery_app.Task = FlaskTask      


celery_app.conf.beat_schedule = {
    'monthly-user-report': {
        'task': 'tasks.send_monthly_report',  
        'schedule': crontab(hour=0, minute=0, day_of_month=1),
    },
    'daily-reminder':{
        'task': 'tasks.send_daily_reminder',
        'schedule': crontab(hour=8, minute=0),
    },
}   
      