from ..core.common_utils import get_env_value


app_label_key = 'SPARROW_ORDER_APP_LABEL'

app_label_key_afs = 'SPARROW_ORDER_AFS_APP_LABEL'

APP_LABEL = get_env_value(app_label_key, 'sparrow_orders')

APP_LABEL_AFS = get_env_value(app_label_key_afs, 'sparrow_orders_afs')
