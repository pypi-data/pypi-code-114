import re

from xmlrpc.client import Boolean

from flask import Flask, request, g
from flask_cors import CORS
from jsons.exceptions import UnfulfilledArgumentError

from witaker.clipboardserver.clipboard_util import AuthorizedClipboardUtilException
from witaker.clipboardserver.clipboard_model import ClipboardRequestBody, clipboard_content_response, clipboard_error_response


app = Flask(__name__)
cors = CORS(app)
## cors = CORS(app, resources={"/clipboard": {"origins": "http://localhost"}})


@app.route('/clipboard', methods=['GET', 'POST'])
def copy_to_clipboard():    
    if request.method == 'GET':
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return clipboard_error_response("Authorization required to fetch clipboard contents").dump(), 401
        else:
            text = app.config['clipboard_util'].paste_text_from_clipboard(auth_key)
            response = clipboard_content_response(text)
            return response.dump()
    elif request.method == 'POST':       
        try:
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return clipboard_error_response("Authorization required to copy text to clipboard").dump(), 401
            else:
                auth_match = re.match(r"Basic\s([\d\w]+)", auth_header)
                if auth_match:
                    auth_key = auth_match[1]
                    req = ClipboardRequestBody.load(request.get_json())
                    print(f"copying text to clipboard [{req.clipboard_request.copy.text[0:24]}...]")
                    app.config['clipboard_util'].copy_text_to_clipboard(auth_key, req.clipboard_request.copy.text)
                    text = app.config['clipboard_util'].paste_text_from_clipboard(auth_key)
                    if (text == req.clipboard_request.copy.text):
                        response = clipboard_content_response(text)
                        return response.dump()
                    else:
                        return clipboard_error_response("Text copy was unsuccessful").dump(), 500
                else:
                    return clipboard_error_response("Authorization scheme must be 'Basic'").dump(), 401
            
        except UnfulfilledArgumentError as e:
            return clipboard_error_response(str(e)).dump(), 400 # Client Error
        except AuthorizedClipboardUtilException as e:
            return clipboard_error_response(str(e)).dump(), 401 # Unauthorized
