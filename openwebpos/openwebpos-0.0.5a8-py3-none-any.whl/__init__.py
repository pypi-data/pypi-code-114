import os

from flask import Flask, render_template

from openwebpos.blueprints import blueprints
from openwebpos.extensions import db
from openwebpos.utils import create_folder, create_file


def OpenWebPOS(instance_dir=None):
    template_dir = 'ui/templates'
    static_dir = 'ui/static'
    base_path = os.path.abspath(os.path.dirname(__file__))

    if instance_dir is None:
        instance_dir = os.path.join(os.getcwd(), 'instance')

    create_folder(folder_path=os.getcwd(), folder_name='instance')
    create_file(file_path=os.getcwd(), file_name='instance/__init__.py')
    create_file(file_path=os.getcwd(), file_name='instance/settings.py', file_mode="w",
                file_content="DB_DIALECT='sqlite'")

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, instance_relative_config=True,
                instance_path=instance_dir)

    app.config.from_pyfile(os.path.join(base_path, 'config/settings.py'))
    app.config.from_pyfile(os.path.join('settings.py'), silent=True)

    db.init_app(app)

    @app.before_first_request
    def before_first_request():
        from openwebpos.extensions import db
        db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html', title='Index')

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
