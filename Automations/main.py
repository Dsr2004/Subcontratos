from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .emails import schedule_api


def start():
    scheduler = BackgroundScheduler(timezone="America/Bogota")
    # scheduler.add_job(schedule_api, 'cron',  hour=13, minute=58)
    scheduler.add_job(schedule_api, 'cron',  hour=13, minute=58)
    scheduler.start()