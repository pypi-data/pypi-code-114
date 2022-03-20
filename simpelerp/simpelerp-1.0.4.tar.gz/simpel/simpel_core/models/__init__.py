from .fields import *  # NOQA
from .mixins import *  # NOQA
from .models import *  # NOQA
from .models import CompanySetting, GeneralSetting
from .registries import *  # NOQA
from .registries import register_setting  # NOQA
from .templates import *  # NOQA

register_setting(GeneralSetting)
register_setting(CompanySetting)
