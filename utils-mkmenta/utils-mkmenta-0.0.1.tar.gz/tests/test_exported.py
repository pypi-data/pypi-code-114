import importlib
import os
import mkutils


def test_all_items_exported():
    ignore_list = ["__init__.py"]
    modules = [m.replace('.py', '') for m in os.listdir('mkutils')
               if m.endswith('.py') and m.startswith('_') and m not in ignore_list]
    for m in modules:
        imported = importlib.import_module(f"mkutils.{m}")
        for item in imported.__all__:
            assert hasattr(mkutils, item)
            assert getattr(mkutils, item) == getattr(imported, item)


def test_import_modules():
    ignore_list = []
    modules = [m.replace('.py', '') for m in os.listdir('mkutils')
               if m.endswith('.py') and not m.startswith('_') and m not in ignore_list]
    for m in modules:
        imported = importlib.import_module(f"mkutils.{m}")
        assert hasattr(mkutils, m)
        assert getattr(mkutils, m) == imported
