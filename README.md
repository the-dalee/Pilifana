Pilifana
========

Collect values of your Pilight devices and display them on your Grafana board.

Pilifana uses the Pilight HTTP API to read current values of all available
devices and save them in a KairosDB. These values can be used later for further
analysis or for displaying on a Grafana board. KairosDB stores the current values
as key-value pairs with the timestamp attached.

Additional KairosDB plug-in is required to display the values in Grafana. For more
information refer to the
[official plugin documentation](https://github.com/grafana/kairosdb-datasource).

## Installation

Use pip3 to install Pilifana:

```
$ sudo pip3 install .
```

## Running

### As standalone application

After installation Pilifana will be available as a standalone application. Run 
following command to start Pilifana:

```
$ pilifana
```

Press `CTRL-C` to exit.

### From Docker container

Use `docker run thedalee/pilifana` (if you built it on your own) to run the container. As the configuration file is inside of the container, you may want to configure Pilifana using following environment variables:

|Name|Type|Example|Meaning|
|----|----|-------|-------|
PILIFANA_PILIGHT_HOST|URL|http://127.0.0.1:5001/|Host and port of your Pilight|
PILIFANA_PILIGHT_AUTH|['basic', 'none']|basic|Type of HTTP authentication for Pilight. 'basic': use HTTP Basic Auth, 'none': don't use authentication|
PILIFANA_PILIGHT_USER|String|user|Pilight username. Remove if your Pilight is not protected by Basic Auth|
PILIFANA_PILIGHT_PASS|String|secret|Pilight password. Remove if your Pilight is not protected by Basic Auth|
PILIFANA_KAIROS_HOST|URL|http://127.0.0.1:8080/|Host and port or your KairosDB|
PILIFANA_KAIROS_AUTH|['basic', 'none']|basic|Type of HTTP authentication for KairosDB. 'basic': use HTTP Basic Auth, 'none': don't use authentication|
PILIFANA_KAIROS_USER|String|user|KairosDB username. Remove if your KairosDB is not protected by Basic Auth|
PILIFANA_KAIROS_PASS|String|secret|KairosDB password. Remove if your KairosDB is not protected by Basic Auth|
PILIFANA_METRIC|String|pilifana|Name of the KairosDB metric. Default: pilifana|

#### Example
```sh
docker run -e PILIFANA_PILIGHT_HOST=http://127.0.0.1:5001/ \
           -e PILIFANA_PILIGHT_AUTH=basic \
           -e PILIFANA_PILIGHT_USER=user \
           -e PILIFANA_PILIGHT_PASS=secret \
           -e PILIFANA_KAIROS_HOST=http://127.0.0.1:8080/ \
           -e PILIFANA_KAIROS_AUTH=basic \
           -e PILIFANA_KAIROS_USER=user \
           -e PILIFANA_KAIROS_PASS=secret \
           -e PILIFANA_METRIC=pilifana \
           thedalee/pilifana
``` 

## Configuration

When installed Pilifana uses settings from your default configration directory 
(usually `/etc/pilifana/config.yaml`). If the settings file could not be found, 
the local configuration file `./configuration/config.yaml` will be used (useful 
for development). If everything else fails, Pilifana will be started using default
configuration. 

You can overwrite the location of the used config file by starting Pilifana with 
command line parameter `--config`.

```bash
$ pilifana --config ./some-config-file.yaml
```