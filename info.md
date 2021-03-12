## somnofy custom component for home assistant

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

run the create_template script if you want one sensors for each hour. See the help options with ```python create_template --help```
