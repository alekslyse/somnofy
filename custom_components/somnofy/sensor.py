"""Support for Somnofy through MQTT."""
from homeassistant.components.arwn.sensor import SomnofySensor
from homeassistant.components import mqtt
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity
from homeassistant.util import slugify
import logging

from .definitions import DEFINITIONS

DOMAIN = "somnofy"

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up Somnofy sensors."""
    _LOGGER.info("Setting up somnofy sensors")

    sensors = []
    for topic in DEFINITIONS:
        sensors.append(SomnofySensor(topic))

    _LOGGER.info("Sensors found: %s", sensors)

    async_add_entities(sensors)


class SomnofySensor(Entity):
    """Representation of a Somnofy sensor that is updated via MQTT."""

    def __init__(self, topic):
        """Initialize the sensor."""

        self._definition = DEFINITIONS[topic]

        self._entity_id = slugify(topic.replace("/", "_"))
        _LOGGER.info("Entity ID: %s", self._entity_id)

        self._topic = topic

        self._name = self._definition.get("name", topic.split("/")[-1])
        self._device_class = self._definition.get("device_class")
        self._enable_default = self._definition.get("enable_default")
        self._unit_of_measurement = self._definition.get("unit")
        self._icon = self._definition.get("icon")
        self._transform = self._definition.get("transform")
        self._state = None

    async def async_added_to_hass(self):
        """Subscribe to MQTT events."""

        @callback
        def message_received(message):
            """Handle new MQTT messages."""

            _LOGGER.info("Somnofy got mqtt %s", message.payload)

            if self._transform is not None:
                self._state = self._transform(message.payload)
            else:
                self._state = message.payload

            self.async_write_ha_state()

        await mqtt.async_subscribe(self.hass, self._topic, message_received, 1)

    @property
    def name(self):
        """Return the name of the sensor supplied in constructor."""
        return self._name

    @property
    def entity_id(self):
        """Return the entity ID for this sensor."""
        return f"sensor.{self._entity_id}"

    @property
    def state(self):
        """Return the current state of the entity."""
        return self._state

    @property
    def device_class(self):
        """Return the device_class of this sensor."""
        return self._device_class

    @property
    def unit_of_measurement(self):
        """Return the unit_of_measurement of this sensor."""
        return self._unit_of_measurement

    @property
    def entity_registry_enabled_default(self) -> bool:
        """Return if the entity should be enabled when first added to the entity registry."""
        return self._enable_default

    @property
    def icon(self):
        """Return the icon of this sensor."""
        return self._icon
