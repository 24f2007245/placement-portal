from celery import Celery, Task
from celery.schedules import crontab
import os
from dotenv import load_dotenv
# import ssl
load_dotenv()

broker_url = os.getenv("REDIS_URL")
result_backend = os.getenv("REDIS_URL")
from app import create_app 

flask_app = create_app()

celery_app = Celery(
    "placement_portal",
    broker=broker_url,
    backend=result_backend,
    include=['mail_server']
)

celery_app.conf.timezone = "Asia/Kolkata"
celery_app.conf.enable_utc = False
celery_app.conf.worker_disable_rate_limits = True
celery_app.conf.worker_prefetch_multiplier = 1
celery_app.conf.worker_log_color = False
celery_app.conf.worker_hijack_root_logger = False
celery_app.conf.CELERYD_FORCE_EXECV = True

# Important for Redis Cloud SSL

# if broker_url.startswith("rediss://"):
#     celery_app.conf.broker_use_ssl = {
#         "ssl_cert_reqs": ssl.CERT_NONE
#     }

#     celery_app.conf.redis_backend_use_ssl = {
#         "ssl_cert_reqs": ssl.CERT_NONE
#     }

    
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
        'schedule': crontab(hour=10, minute=0),         #minute='*/2' | hour=10, minute=0
    },
}   