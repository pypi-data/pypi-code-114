from gview import plotDataAPI
from .app_celery_init import create_app

# initialize app
app = create_app()

# resgister blueprints
from . import index,host,plotDataAPI
app.register_blueprint(index.bp)
app.register_blueprint(host.bp)
app.register_blueprint(plotDataAPI.bp)
