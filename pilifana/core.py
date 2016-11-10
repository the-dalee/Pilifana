import schedule
import time
import clients.pilight
import clients.kairosdb
import conversion.structure

def job():
    client = clients.pilight.PilightClient('192.168.0.155:5001')
    kairos = clients.kairosdb.KairosdbClient('127.0.0.1:8080')
    flattener = conversion.structure.Flattener()
    data = flattener.flatten(client.get())
    kairos.set(data)


def run(interval):
    schedule.every(interval).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)