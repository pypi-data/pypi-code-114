# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['flask_cognito_lib', 'flask_cognito_lib.services']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.0,<3.0', 'PyJWT[crypto]>=2.0,<3.0', 'requests>=2.0,<3.0']

setup_kwargs = {
    'name': 'flask-cognito-lib',
    'version': '0.1.3',
    'description': 'A Flask extension that supports protecting routes with AWS Cognito following OAuth 2.1 best practices',
    'long_description': '# Protect Flask routes with AWS Cognito\n\nA Flask extension that supports protecting routes with AWS Cognito following [OAuth 2.1 best practices](https://oauth.net/2.1/). That means the full authorization code flow, including Proof Key for Code Exchange (RFC 7636) to prevent Cross Site Request Forgery (CRSF), along with secure storage of access tokens in HTTP only cookies (to prevent Cross Site Scripting attacks), and additional `nonce` validation (if using ID tokens) to prevent replay attacks.\n\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install:\n\n```bash\npip install flask-coginito-lib\n```\n\n\n## Quick start\n\nA complete example Flask application is provided in [`/example`](example/) including instructions on setting up a Cognito User Pool. Assuming a Cognito user pool has been setup, with an app client (with Client ID and Secret), get started as follows:\n\n```python\nfrom flask import Flask, jsonify, redirect, session, url_for\n\nfrom flask_cognito_lib import CognitoAuth\nfrom flask_cognito_lib.decorators import (\n    auth_required,\n    cognito_login,\n    cognito_login_callback,\n    cognito_logout,\n)\n\napp = Flask(__name__)\n\n# Configuration required for CognitoAuth\napp.config["AWS_REGION"] = "eu-west-1"\napp.config["AWS_COGNITO_USER_POOL_ID"] = "eu-west-1_qwerty"\napp.config["AWS_COGNITO_DOMAIN"] = "https://app.auth.eu-west-1.amazoncognito.com"\napp.config["AWS_COGNITO_USER_POOL_CLIENT_ID"] = "asdfghjkl1234asdf"\napp.config["AWS_COGNITO_USER_POOL_CLIENT_SECRET"] = "zxcvbnm1234567890"\napp.config["AWS_COGNITO_REDIRECT_URL"] = "https://example.com/postlogin"\napp.config["AWS_COGNITO_LOGOUT_URL"] = "https://example.com/postlogout"\n\nauth = CognitoAuth(app)\n\n\n@app.route("/login")\n@cognito_login\ndef login():\n    # A simple route that will redirect to the Cognito Hosted UI.\n    # No logic is required as the decorator handles the redirect to the Cognito\n    # hosted UI for the user to sign in.\n    pass\n\n\n@app.route("/postlogin")\n@cognito_login_callback\ndef postlogin():\n    # A route to handle the redirect after a user has logged in with Cognito.\n    # This route must be set as one of the User Pool client\'s Callback URLs in\n    # the Cognito console and also as the config value AWS_COGNITO_REDIRECT_URL.\n    # The decorator will store the validated access token in a HTTP only cookie\n    # and the user claims and info are stored in the Flask session:\n    # session["claims"] and session["user_info"].\n    # Do anything login after the user has logged in here, e.g. a redirect\n    return redirect(url_for("claims"))\n\n\n@app.route("/claims")\n@auth_required()\ndef claims():\n    # This route is protected by the Cognito authorisation. If the user is not\n    # logged in at this point or their token from Cognito is no longer valid\n    # a 401 Authentication Error is thrown, which is caught here a redirected\n    # to login.\n    # If their session is valid, the current session will be shown including\n    # their claims and user_info extracted from the Cognito tokens.\n    return jsonify(session)\n\n\n@app.route("/admin")\n@auth_required(groups=["admin"])\ndef admin():\n    # This route will only be accessible to a user who is a member of all of\n    # groups specified in the "groups" argument on the auth_required decorator\n    # If they are not, a CognitoGroupRequiredError is raised which is handled\n    # below\n    return jsonify(session["claims"]["cognito:groups"])\n\n\n@app.route("/logout")\n@cognito_logout\ndef logout():\n    # Logout of the Cognito User pool and delete the cookies that were set\n    # on login.\n    # No logic is required here as it simply redirects to Cognito.\n    pass\n\n\n@app.route("/postlogout")\ndef postlogout():\n    # This is the endpoint Cognito redirects to after a user has logged out,\n    # handle any logic here, like returning to the homepage.\n    # This route must be set as one of the User Pool client\'s Sign Out URLs.\n    return redirect(url_for("home"))\n\n\nif __name__ == "__main__":\n    app.run()\n```\n\n\n## Development\n\nPrequisites:\n\n* [poetry](https://python-poetry.org/)\n* [pre-commit](https://pre-commit.com/)\n\nThe Makefile includes helpful commands setting a development environment, get started by installing the package into a new environment and setting up pre-commit by running `make install`. Run `make help` to see additional available commands (e.g. linting, testing and so on).\n\n* [Pytest](https://docs.pytest.org/en/6.2.x/) is used for testing the application (see `/tests`).\n* Code is linted using [flake8](https://flake8.pycqa.org/en/latest/)\n* Code formatting is validated using [Black](https://github.com/psf/black)\n* [pre-commit](https://pre-commit.com/) is used to run these checks locally before files are pushed to git\n* The [Github Actions pipeline](.github/workflows/pipeline.yml) runs these checks and tests\n\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate and ensure 100% test coverage.\n\n\n## Credits\n\nThis work started as a fork of the unmaintained [Flask-AWSCognito](https://github.com/cgauge/Flask-AWSCognito) extension, revising the implementation following OAuth 2.1 recommendations, with inspiration from [flask-cognito-auth](https://github.com/shrivastava-v-ankit/flask-cognito-auth). Whilst there are serveral Cognito extensions available for Flask, none of those implement OAuth 2.1 recommendations, with some plugins not even actively maintained.\n',
    'author': 'mblackgeo',
    'author_email': '18327836+mblackgeo@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mblackgeo/flask-cognito-lib',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
