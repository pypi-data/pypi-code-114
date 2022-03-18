"""
server.py
====================================
Mock server for testing REST API.
"""

import os
from flask import Flask, request
from flask_restful import Resource, Api


class PartEndpoint(Resource):
    """
    Part data API endpoint class.

    Resource used in Flask app to mock REST API.

    """

    def get(self):
        """
        REST API get request to return part data.

        Returns
        -------
        tuple, int
            part data (json), status code

        """
        json_data = {
            "partId": "Part_I3DR_test_003",
            "source": "I3DR_test",
            "identifiedTime": 1647606457463.4841,
            "partData": [
                {
                    "key": "supplier",
                    "string": "I3DR"
                }
            ],
            "images": [
                {
                    "imageFileName": "I3DR_test_003.tif",
                    "capturedBy": "I3DR_test_camera",
                    "capturedTime": 1647606457463.4841,
                    "positionX": 0,
                    "positionY": 0,
                    "positionZ": 0,
                    "dimensionX": 5000,
                    "dimensionY": 1,
                    "dimensionZ": 0,
                    "defects": [
                        {
                            "defectType": {
                                "code": "315"
                            },
                            "identifiedBy": "I3DR_test_user",
                            "identifiedTime": 1647606457463.4841,
                            "positionX": 0, "positionY": 0,
                            "positionZ": 0, "dimensionX": 0,
                            "dimensionY": 0, "dimensionZ": 0
                        }
                    ]
                }
            ]}
        return json_data, 200  # return data and 200 OK code

    def post(self):
        """
        REST API post request to accept part data.

        Returns
        -------
        tuple, int
            part data (json), status code

        """
        json_data = request.json
        # TODO validate json data
        # return data with 201 created success code
        return json_data, 201


def create_app(test_config=None):
    """
    Create Flask app

    Create and configure the app to mockup server for iMath REST API.

    Parameters
    ----------
    test_config:
        Test config

    Returns
    -------
    app, api
        Flask App, Flask API

    """

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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

    api = Api(app)

    @app.route('/')
    def index():
        page = """
            <h1>Welcome to iMath Requests test server</h1>
            <h3>The following API endpoints are available:</h3>
            <ul>
                <li>/part</li>
            </ul>
        """
        return page

    api.add_resource(
        PartEndpoint, '/imath-rest-backend/part')

    return app, api


if __name__ == "__main__":
    app, api = create_app()
    app.run()
