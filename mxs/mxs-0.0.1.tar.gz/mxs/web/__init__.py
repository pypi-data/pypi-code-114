"""
MXS is the Math eXploration Solver.
Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""

import os

from flask import Flask

from mxs.web import pattern


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    """
    __name__ is the name of the current Python module.
    The app needs to know where it’s located to set up some paths,
    and __name__ is a convenient way to tell it that.

    instance_relative_config=True tells the app that configuration files are
    relative to the instance folder. The instance folder is located outside
    the falsker package and can hold local data that shouldn’t be committed
    to version control, such as configuration secrets and the database file.
    """

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.register_blueprint(pattern.bp)

    return app
