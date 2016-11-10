import schedule
import time


def job():
    print("Running")


def run(interval):
    schedule.every(interval).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
