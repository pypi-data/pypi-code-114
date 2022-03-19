
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.coupon_api import CouponApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from soracom_sandbox.api.coupon_api import CouponApi
from soracom_sandbox.api.operator_api import OperatorApi
from soracom_sandbox.api.order_api import OrderApi
from soracom_sandbox.api.stats_api import StatsApi
from soracom_sandbox.api.subscriber_api import SubscriberApi
