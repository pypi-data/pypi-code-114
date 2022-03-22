from ..core.common_utils import get_env_value


app_label_key = 'SPARROW_DISTRIBUTE_APP_LABEL'

APP_LABEL = get_env_value(app_label_key, 'sparrow_distribute')
