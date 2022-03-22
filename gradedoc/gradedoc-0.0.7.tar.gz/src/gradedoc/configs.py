from dynaconf import Dynaconf

config = Dynaconf(
    settings_files=["config.yaml", "config_lab_specific.yaml"],
    merge_enabled=True,
)
