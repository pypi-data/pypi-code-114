# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cornflower']

package_data = \
{'': ['*']}

install_requires = \
['kombu>=5.2.3,<6.0.0', 'pika>=1.2.0,<2.0.0', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'cornflower',
    'version': '0.1.0',
    'description': 'Library for writting simple AMQP handlers with type hints and pydantic support',
    'long_description': '## Cornflower\n### Library for writing RabbitMQ message handlers with [pydantic](https://github.com/samuelcolvin/pydantic) validation.\n\n\n## Example use:\n\n\nHandler callback can accept zero or one argument of `pydantic.BaseModel` type. Message body will be validated automatically against specified schema.\n\n```python\nfrom cornflower import MessageQueue, OutputMessage, MessageDeliveryMode\nfrom pydantic import BaseModel\n\n\nclass UserMessage(BaseModel):\n    username: str\n    message: str\n\n\nqueue = MessageQueue(url="amqp://user:password@host:port")\n\n\n@queue.listen(routing_key="user.registered")\ndef handle_user_register(message: UserMessage) -> None:\n    # do something with validated message\n    ...\n\n\n@queue.listen(routing_key="user.login")\ndef handle_user_login() -> None:\n    # callback with no arguments, handle message without\n    # validating its body\n    \n    # sending message\n    user_message = UserMessage(username="example", message="this is example")\n    \n    queue.dispatch(\n        message=OutputMessage(\n            body=user_message.dict(),\n            routing_key="user.logout",\n            delivery_mode=MessageDeliveryMode.PERSISTENT,\n        )\n    )\n\n\nif __name__ == "__main__":\n    queue.run()\n```\n\n\n## Optional configuration\n\n```python\nfrom cornflower import MessageQueue\nfrom cornflower.options import QueueOptions, TransportOptions, ConsumerOptions\n\nqueue = MessageQueue(\n    queue_options=QueueOptions(\n        durable=True,\n        exclusive=False,\n        auto_delete=False,\n    ),\n    consumer_options=ConsumerOptions(\n        prefetch_count=10\n    ),\n    transport_options=TransportOptions(\n        confirm_publish=True,\n    )\n)\n```',
    'author': 'jakub-figat',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jakub-figat/cornflower',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
