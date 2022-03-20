"""Top-level package for siphon."""

__author__ = """Mitchell Lisle"""
__email__ = 'm.lisle90@gmail.com'
__version__ = '0.6.1'


from siphon.database.aiopostgres import AioPostgres, Record  # noqa: F401
from siphon.database.mysql import AioMySQL, MySQLConfig  # noqa: F401
from siphon.database.postgres import Postgres, PostgresConfig  # noqa: F401
from siphon.logger import logger  # noqa: F401
from siphon.queue.aioqueue import CollectedError  # noqa: F401
from siphon.queue.aioqueue import (AioQueue, TypedAioQueue,  # noqa: F401
                                   queuecollect)
from siphon.queue.violations import RaiseOnViolation  # noqa: F401
from siphon.queue.violations import (DiscardOnViolation,  # noqa: F401
                                     ViolationStrategy)
from siphon.rabbit.aiorabbit import (AioRabbitConsumer,  # noqa: F401
                                     RabbitConfig)
