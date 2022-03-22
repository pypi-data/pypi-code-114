
from six import with_metaclass
from pluggy import PluginManager
from allure_commons import _hooks
import allure_commons
import pytest


class MetaPluginManager(type):
    @staticmethod
    def get_plugin_manager():
        if not hasattr(MetaPluginManager, 'plugin_manager'):

            MetaPluginManager.plugin_manager = PluginManager('allure')
            MetaPluginManager.plugin_manager.add_hookspecs(_hooks.AllureUserHooks)
            MetaPluginManager.plugin_manager.add_hookspecs(_hooks.AllureDeveloperHooks)

        return MetaPluginManager.plugin_manager

    def __getattr__(cls, attr):
        pm = MetaPluginManager.get_plugin_manager()
        return getattr(pm, attr)


class plugin_manager(with_metaclass(MetaPluginManager)):
    pass



@pytest.mark.tryfirst
def pytest_configure(config):
    global pytest_config
    pytest_config = config
    allure_commons.plugin_manager = plugin_manager
    allure_commons._core.plugin_manager = plugin_manager
    allure_commons.reporter.plugin_manager = plugin_manager