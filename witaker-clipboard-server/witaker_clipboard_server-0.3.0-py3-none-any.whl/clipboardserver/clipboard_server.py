import re

from flask import Flask, request
from flask_cors import CORS
from jsons.exceptions import UnfulfilledArgumentError

from witaker.clipboardserver import (
    name,
    version,
    AuthorizedClipboardUtilException,
    ClipboardRequestBody,
    PingResponseBody,
    PingErrorBody,
    clipboard_content_response,
    clipboard_error_response,
)


app = Flask(__name__)
cors = CORS(app)
## cors = CORS(app, resources={"/clipboard": {"origins": "http://localhost"}})


def check_for_auth_header(headers, clipboard_util):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return (False, "Authorization required")
    else:
        auth_match = re.match(r"^Basic\s([\d\w\+\/]+={0,2}$)", auth_header)
        if auth_match:
            auth_key = auth_match[1]
            if clipboard_util.auth_key_matches(auth_key):
                return (True, auth_key)
            else:
                return (False, "Authentication key was invalid")
        else:
            return (False, "Authorization scheme must be 'Basic'")


@app.route("/ping", methods=["GET"])
def ping():
    auth_is_valid, message = check_for_auth_header(
        request.headers, app.config["clipboard_util"]
    )
    if auth_is_valid:

        return PingResponseBody(f"{name} {version}").dump
    else:
        return PingErrorBody(message), 401


@app.route("/clipboard", methods=["GET", "POST"])
def copy_to_clipboard():
    auth_is_valid, message = check_for_auth_header(
        request.headers, app.config["clipboard_util"]
    )
    if auth_is_valid:
        if request.method == "GET":
            text = app.config["clipboard_util"].paste_text_from_clipboard(auth_key)
            response = clipboard_content_response(text)
            return response.dump()
        elif request.method == "POST":
            try:
                auth_key = message
                req = ClipboardRequestBody.load(request.get_json())
                print(
                    f" + Copying text to clipboard [{req.clipboard_request.copy.text[0:24]}...]"
                )
                app.config["clipboard_util"].copy_text_to_clipboard(
                    auth_key, req.clipboard_request.copy.text
                )
                text = app.config["clipboard_util"].paste_text_from_clipboard(auth_key)
                if text == req.clipboard_request.copy.text:
                    response = clipboard_content_response(text)
                    return response.dump()
                else:
                    return (
                        clipboard_error_response("Text copy was unsuccessful").dump(),
                        500,
                    )
            except UnfulfilledArgumentError as e:
                return clipboard_error_response(str(e)).dump(), 400  # Client Error
            except AuthorizedClipboardUtilException as e:
                return clipboard_error_response(str(e)).dump(), 401  # Unauthorized
    else:
        return clipboard_error_response(message).dump(), 401