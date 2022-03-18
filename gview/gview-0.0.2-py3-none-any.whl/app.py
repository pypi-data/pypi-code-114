from app_celery_init import create_app
from utils import argParser

# initialize app
app = create_app()

# resgister blueprints
import index,host
app.register_blueprint(index.bp)
app.register_blueprint(host.bp)

