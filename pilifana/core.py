import schedule
import time
import pilifana.clients.pilight
import pilifana.clients.kairosdb
import pilifana.conversion.structure


def job():
    client = pilifana.clients.pilight.PilightClient('192.168.0.155:5001') 
    kairos = pilifana.clients.kairosdb.KairosdbClient('127.0.0.1:8080')
    flattener =  pilifana.conversion.structure.Flattener()
    data = flattener.flatten(client.get())
    kairos.set(data)


def run(interval):
    schedule.every(interval).seconds.do(job)
    while True:
        try:
            time.sleep(1)
            schedule.run_pending()
        except KeyboardInterrupt:
            print('Closing Pilifana...')
            return 
        except Exception as e:
            print(e)
