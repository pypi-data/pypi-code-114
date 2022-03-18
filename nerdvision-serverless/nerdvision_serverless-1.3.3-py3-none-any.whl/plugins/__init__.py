import logging
from importlib import import_module

from nerdvision import TYPES
from nerdvision.NerdVision import NerdVision

if TYPES:
    from typing import List

NV_PLUGINS = [
    'nerdvision.plugins.datadog.DatadogAPMPlugin',
    'nerdvision.plugins.sentry.SentryErrorPlugin'
]

our_logger = logging.getLogger("nerdvision")


def plugin_generator(configured):
    for plugin in configured:
        try:
            module, cls = plugin.rsplit(".", 1)
            yield getattr(import_module(module), cls)
            our_logger.debug('Did import default integration %s', plugin)
        except (DidNotEnable, SyntaxError) as e:
            our_logger.debug(
                "Did not import default integration %s: %s", plugin, e
            )


def load_plugins(nv):
    # type: (NerdVision) -> List[str]
    loaded = []  # type: List[str]
    for plugin in plugin_generator(NV_PLUGINS):
        try:
            plugin_instance = plugin()
            plugin_instance.load_plugin(nv)
            loaded.append(plugin_instance.name)
        except Exception as e:
            our_logger.debug("Could not load plugin %s: %s", plugin, e)
    return loaded


class DidNotEnable(Exception):
    """
    The integration could not be enabled due to a trivial user error like
    `flask` not being installed for the `FlaskIntegration`.
    """


class Plugin(object):
    """
    This type defines a plugin for NerdVision, these plugins allow for extensions to how NerdVision decorates data and captures exceptions.
    """

    def __init__(self):
        # type:  ()-> None
        super(Plugin, self).__init__()
        self._name = self.__class__.__name__

    @property
    def name(self):
        return self._name

    def load_plugin(self, nerdvision):
        # type: (NerdVision) -> None
        pass

    @name.setter
    def name(self, value):
        self._name = value
