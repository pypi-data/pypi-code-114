import os
import shutil

default_module_configs = os.path.join(os.path.dirname(os.path.realpath(__file__)), '.', 'configs')

def ensure_base_configs(config_dir: str):
    """
    Ensure that the base configs are present.
    """
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    for f in os.listdir(default_module_configs):
        if not os.path.exists(os.path.join(config_dir, f)):
            shutil.copytree(os.path.join(default_module_configs, f), os.path.join(config_dir, f))
    
