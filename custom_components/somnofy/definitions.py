"""Definitions for Somnofy sensors added to MQTT."""

from homeassistant.const import TEMP_CELSIUS, DEVICE_CLASS_TEMPERATURE


DEFINITIONS = {
    "somnofy/VTBMWLSYHR/environment": {
        "name": "Temperature",
        "enable_default": True,
        "device_class": DEVICE_CLASS_TEMPERATURE,
        "unit": TEMP_CELSIUS,
    },
}
