## nordpool custom component for home assistant

## Installation

### Option 1: HACS

Under HACS -> Integrations, select "+", search for `somnofy` and install it.


### Option 2: Manual

From the [latest release](https://github.com/alekslyse/somnofy/releases)

```bash
cd YOUR_HASS_CONFIG_DIRECTORY    # same place as configuration.yaml
mkdir -p custom_components/somnofy
cd custom_components/somnofy
unzip somnofy.X.Y-Z.zip
```

### Usage

Set up the sensor using the webui or use a yaml.

The sensors tries to set some sane default so a minimal setup can be

```
sensor:
  - platform: somnofy
```



in configuration.yaml

```
somnofy:

sensor:
  - platform: somnofy

    SERIAL: 123456

```


run the create_template script if you want one sensors for each hour. See the help options with ```python create_template --help``` you can run the script anyhere python is installed. (install the required packages pyyaml and click using `pip install packagename`)
