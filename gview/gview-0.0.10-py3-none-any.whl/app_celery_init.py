from flask import Flask
from celery import Celery

# flask factory
def create_app():
    app = Flask(__name__)
    app.config['CELERY_broker_url'] = 'redis://localhost:6379/0'
    app.config['result_backend'] = 'redis://localhost:6379/0'
    return app

# celery factory
def make_celery(app):
    celery = Celery(app.name, broker=app.config['CELERY_broker_url'], backend=app.config['result_backend'])
    return celery