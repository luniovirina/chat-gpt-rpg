import os
from dynaconf import Dynaconf

current_directory = os.path.dirname(os.path.realpath(__file__))
settings = Dynaconf(
    root_path=current_directory,
    envvar_prefix="DYNACONF",
    settings_files=["config/settings.toml", "config/.secrets.toml"],
    envaronments=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
