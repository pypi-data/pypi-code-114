import os
import certifi
from flask import Flask

from eisenradio.instance.config_apfac import write_config
from eisenradio.api import api

# android ssl fix
os.environ['SSL_CERT_FILE'] = certifi.where()

app = Flask(__name__)

with app.app_context():
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    api.init_app(app)
    """------------- EisenradioAndroid -------------------"""
    # android made trouble with app factory (definition) and __init__.py imports,
    # so we do not run from package wsgi.py as usual, this module is used as service in the build process
    # and main.py calls it (mActivity stuff)
    print('\n\t---> WITH app_context <---\n')
    write_config('android')

    # helper stuff
    from eisenradio.lib.platform_helper import main as start_frontend
    from eisenradio.lib.eisdb import install_new_db as create_install_db
    # Import parts of the application, separated by routes
    from eisenradio.eisenhome import routes as home_routes
    from eisenradio.eisenutil import routes as util_routes

    # Register Blueprints (pointer to parts of the application, subprojects in production)
    app.register_blueprint(home_routes.eisenhome_bp)
    app.register_blueprint(util_routes.eisenutil_bp)

    create_install_db(app.config['DATABASE'])
    print(f"""------------- DATABASE -----{app.config['DATABASE']}--------------""")

if __name__ == "__main__":
    app.run(host='localhost', port=5050)
