from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .emails import schedule_api


def start():
    scheduler = BackgroundScheduler(timezone="America/Bogota")
    # scheduler.add_job(schedule_api, 'cron',  hour=16, minute=10)
    scheduler.add_job(schedule_api, 'interval',  seconds=15)
    scheduler.start()