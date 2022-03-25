from __future__ import annotations

from atoti_core import MissingPluginError, get_active_plugins


def register_active_plugins() -> None:
    """Register all the active plugins."""
    for plugin in get_active_plugins().values():
        plugin.static_init()


def is_plugin_active(plugin_key: str) -> bool:
    """Return whether the plugin is active or not."""
    return plugin_key in get_active_plugins()


def ensure_plugin_active(plugin_key: str) -> None:
    if not is_plugin_active(plugin_key):
        raise MissingPluginError(plugin_key)
