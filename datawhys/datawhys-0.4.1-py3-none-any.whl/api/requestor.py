from base64 import b64encode
import json
import platform
import warnings

import datawhys
from datawhys import error, utils
from datawhys.api import clients
from datawhys.api.util import encode_multipart


class APIRequestor(object):
    def __init__(self, key=None, client=None, api_base=None, auth_enabled=None):
        self.api_base = api_base or datawhys.api_base
        self.api_key = key
        self.auth_enabled = datawhys.auth_enabled

        if auth_enabled is not None:
            self.auth_enabled = auth_enabled

        self._default_proxy = None

        from datawhys import proxy, verify_ssl_certs as verify

        if client:
            self._client = client
        elif datawhys.default_http_client:
            self._client = datawhys.default_http_client
            if proxy != self._default_proxy:
                warnings.warn(
                    "datawhys.proxy was updated after sending a "
                    "request - this is a no-op. To use a different proxy, "
                    "set datawhys.default_http_client to a new client "
                    "configured with the proxy."
                )
        else:
            datawhys.default_http_client = clients.new_default_http_client(
                verify_ssl_certs=verify, proxy=proxy
            )
            self._client = datawhys.default_http_client
            self._default_proxy = proxy

    def request(self, method, url, params=None, headers=None):
        rbody, rcode, rheaders = self.request_raw(method.lower(), url, params, headers)

        resp = self.interpret_response(rbody, rcode, rheaders)
        return resp

    def handle_error_response(self, rbody, rcode, resp, rheaders):
        try:
            error_data = {"type": resp["type"], "message": resp["message"]}

            code = resp.get("code", None)
            if code is not None:
                error_data["code"] = code
        except (KeyError, TypeError):
            raise error.APIError(
                "Invalid response object from API: %r "
                "(HTTP response code was %d)" % (rbody, rcode),
                rbody,
                rcode,
                resp,
                rheaders,
            )

        msg = error_data.get("message", None)

        if rcode == 401:
            raise error.AuthenticationError(msg, rbody, rcode, resp, rheaders, code)

        elif rcode == 402:
            eType = error_data["type"]
            raise error.ProcessingError(msg, rbody, rcode, resp, rheaders, code, eType)

        elif rcode == 403:
            raise error.PermissionError(msg, rbody, rcode, resp, rheaders, code)

        else:
            raise error.APIError(msg, rbody, resp, rheaders)

    def request_headers(self, api_key):
        user_agent = "Mondobrain/v1 PythonBindings/%s" % (datawhys.__version__,)

        ua = {
            "bindings_version": datawhys.__version__,
            "lang": "python",
            "publisher": "datawhys",
            "httplib": "requests",
            "lang_version": platform.python_version(),
            "platform": platform.platform(),
            "uname": " ".join(platform.uname()),
        }

        headers = {
            "X-Mondobrain-Client-User-Agent": json.dumps(ua),
            "User-Agent": user_agent,
            "Content-Type": "application/json",
        }

        # Only add authorization header if auth is enabled
        if self.auth_enabled:
            # TODO: make this Bearer without base64 once solve api
            # supports non-basic auth
            creds = ("%s:" % api_key).encode()
            headers["Authorization"] = "Basic %s" % b64encode(creds).decode("ascii")

        return headers

    def request_raw(self, method, url, params=None, supplied_headers=None):
        """
        Mechanism for issuing an API call
        """
        if self.api_key:
            my_api_key = self.api_key
        else:
            from datawhys import api_key

            my_api_key = api_key

        if my_api_key is None and datawhys.auth_enabled:
            raise error.AuthenticationError(
                "No API key provided. (HINT: set your API key using "
                '"datawhys.api_key = <API-KEY>"). You can generate API keys '
                "from the DataWhys dashboard.  See https://api.datawhys.ai/redoc "
                "for details, or email support@datawhys.ai if you have any "
                "questions."
            )

        abs_url = "%s%s" % (self.api_base, url)

        if (
            supplied_headers is not None
            and supplied_headers.get("Content-Type") == "multipart/form-data"
        ):
            post_data, content_type = encode_multipart(params)
            supplied_headers["Content-Type"] = content_type
        else:
            params = {k: v for k, v in params.items() if v is not None}
            post_data = json.dumps(params)

        headers = self.request_headers(my_api_key)
        if supplied_headers is not None:
            for key, value in supplied_headers.items():
                headers[key] = value

        utils.log_info("Request to DataWhys api", method=method, path=abs_url)
        utils.log_debug("Post details", post_data=params)

        rbody, rcode, rheaders = self._client.request_with_polling(
            method, abs_url, headers, post_data
        )

        utils.log_info("DataWhys API response", path=abs_url, response_code=rcode)
        utils.log_debug("API response body", body=rbody)

        return rbody, rcode, rheaders

    def interpret_response(self, rbody, rcode, rheaders):
        try:
            if hasattr(rbody, "decode"):
                rbody = rbody.decode("utf-8")

            data = json.loads(rbody)
        except Exception:
            raise error.APIError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (rbody, rcode),
                rbody,
                rcode,
                headers=rheaders,
            )

        if not 200 <= rcode < 300:
            self.handle_error_response(rbody, rcode, data, rheaders)

        return data
