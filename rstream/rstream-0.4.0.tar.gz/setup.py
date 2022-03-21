# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rstream']

package_data = \
{'': ['*']}

install_requires = \
['uamqp>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'rstream',
    'version': '0.4.0',
    'description': 'A python client for RabbitMQ Streams',
    'long_description': "# RabbitMQ Stream Python Client\n\nA Python asyncio-based client for [RabbitMQ Streams](https://github.com/rabbitmq/rabbitmq-server/tree/master/deps/rabbitmq_stream)  \n_This is a work in progress_\n\n## Install\n\n```bash\npip install rstream\n```\n\n## Quick start\n\nPublishing messages:\n\n```python\nimport asyncio\nfrom rstream import Producer, AMQPMessage\n\nasync def publish():\n    async with Producer('localhost', username='guest', password='guest') as producer:\n        await producer.create_stream('mystream')\n\n        for i in range(100):\n            amqp_message = AMQPMessage(\n                body='hello: {}'.format(i),\n            )\n            await producer.publish('mystream', amqp_message)\n\nasyncio.run(publish())\n```\n\nConsuming messages:\n\n```python\nimport asyncio\nimport signal\nfrom rstream import Consumer, amqp_decoder, AMQPMessage\n\nasync def consume():\n    consumer = Consumer(\n        host='localhost',\n        port=5552,\n        vhost='/',\n        username='guest',\n        password='guest',\n    )\n\n    loop = asyncio.get_event_loop()\n    loop.add_signal_handler(signal.SIGINT, lambda: asyncio.create_task(consumer.close()))\n\n    def on_message(msg: AMQPMessage):\n        print('Got message: {}'.format(msg.body))\n\n    await consumer.start()\n    await consumer.subscribe('mystream', on_message, decoder=amqp_decoder)\n    await consumer.run()\n\nasyncio.run(consume())\n```\n\nConnecting with SSL:\n\n```python\nimport ssl\n\nssl_context = ssl.SSLContext()\nssl_context.load_cert_chain('/path/to/certificate.pem', '/path/to/key.pem')\n\nproducer = Producer(\n    host='localhost',\n    port=5551,\n    ssl_context=ssl_context,\n    username='guest',\n    password='guest',\n)\n```\n\n## TODO\n\n- [ ] Documentation\n- [ ] Handle `MetadataUpdate` and reconnect to another broker on stream configuration changes\n- [ ] AsyncIterator protocol for consumer\n- [ ] Add frame size validation\n",
    'author': 'George Fortunatov',
    'author_email': 'qweeeze@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/qweeze/rstream',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
