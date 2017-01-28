import schedule
import time
import pilifana.clients.pilight
import pilifana.clients.kairosdb
import pilifana.conversion.structure
import logging


def job(config):
    pilight_host = config.get('services.pilight.host', default="http://127.0.0.1:5001", env='PILIFANA_PILIGHT_HOST')
    pilight_auth = config.get('services.pilight.authentication', env='PILIFANA_PILIGHT_AUTH', default='none') == "basic"
    pilight_username = config.get('services.pilight.username', env='PILIFANA_PILIGHT_USER') if pilight_auth else None
    pilight_password = config.get('services.pilight.password', env='PILIFANA_PILIGHT_PASS') if pilight_auth else None
    kairos_host = config.get('services.kairosdb.host', default="http://127.0.0.1:9004", env='PILIFANA_PILIGHT_HOST')
    kairos_auth = config.get('services.kairosdb.authentication', env='PILIFANA_KAIROS_AUTH', default='none') == "basic"
    kairos_username = config.get('services.kairosdb.username', env='PILIFANA_KAIROS_USER') if kairos_auth else None
    kairos_password = config.get('services.kairosdb.password', env='PILIFANA_KAIROS_PASS') if kairos_auth else None
    metric = config.get('pilifana.metric', default='pilifana', env='PILIFANA_METRIC')

    logging.debug('Connecting to pilight host {0} using authentication {1}'.format(pilight_host, pilight_auth))
    client = pilifana.clients.pilight.PilightClient(pilight_host,
                                                    username=pilight_username,
                                                    password=pilight_password)
    logging.debug('Connecting to kairos host {0} using authentication {1}'.format(kairos_host, kairos_auth))
    kairos = pilifana.clients.kairosdb.KairosdbClient(kairos_host,
                                                      username=kairos_username,
                                                      password=kairos_password)

    flattener =  pilifana.conversion.structure.Flattener()
    data = flattener.flatten(client.get())
    kairos.set(metric, data)


def run(config):

    interval = int(config.get('pilifana.interval', default=1, env='PILIFANA_INTERVAL'))
    logging.debug('Update interval: {0}'.format(interval))
    schedule.every(interval).seconds.do(job, config)

    while True:
        try:
            time.sleep(1)
            schedule.run_pending()
        except KeyboardInterrupt:
            logging.info('Closing Pilifana...')
            return 
        except Exception as e:
            logging.error(e)
