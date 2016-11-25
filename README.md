Pilifana
========

Collect values of your Pilight devices and display them on your Grafana board.

Pilifana uses the Pilight HTTP API to read current values of all available
devices and save them in a CairosDB. These values can be used later for further
analysis or for displaying on a Grafana board. CairosDB stores the current values
as key-value pairs with the timestamp attached.

Additional CairosDB plug-in is required to display the values in Grafana. For more
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


## Configuration

When installed Pilifana uses settings from your default configration directory 
(usually `/etc/pilifana/config.yaml`). If the settings file could not be found, 
the local configuration file `./configuration/config.yaml` will be used (useful 
for development). If everything else fails, Pilifana will be started using default
configuration. 

You can overwrite the location of the used config file by starting Pilifana with 
bcommand line parameter `--config`.

```bash
$ pilifana --config ./some-config-file.yaml
```