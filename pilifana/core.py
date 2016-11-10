import schedule
import time
import clients.pilight
import conversion.structure

def job():
    client = clients.pilight.PilightClient('192.168.0.155:5001')
    flattener = conversion.structure.Flattener()
    print(flattener.flatten(client.get()))


def run(interval):
    schedule.every(interval).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
