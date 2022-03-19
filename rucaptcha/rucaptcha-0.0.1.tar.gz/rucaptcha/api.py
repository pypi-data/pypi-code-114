import json
from base64 import b64encode
import time
import logging

from urllib3 import PoolManager

from .errors import ConfigurationError, ResultTimeout, ResultNotReady

__all__ = ["RucaptchaApi"]
VALID_TASK_TYPES = ["image", "text"]
DEFAULT_TASK_TIMEOUT = 60
VALID_LANGS = set(
    [
        "ar",
        "az",
        "be",
        "bg",
        "bn",
        "bs",
        "ca",
        "cs",
        "da",
        "de",
        "el",
        "en",
        "es",
        "et",
        "fa",
        "fi",
        "fil",
        "fr",
        "he",
        "hi",
        "hr",
        "hu",
        "hy",
        "id",
        "it",
        "ja",
        "ka",
        "kk",
        "ko",
        "lt",
        "lv",
        "mk",
        "ml",
        "mr",
        "ms",
        "my",
        "nb",
        "ne",
        "nl",
        "pa",
        "pl",
        "pt",
        "ro",
        "ru",
        "sk",
        "sl",
        "sr",
        "sv",
        "te",
        "th",
        "tr",
        "uk",
        "uz",
        "vi",
        "zh",
    ]
)
SOFTWARE_ID = 2373
ERROR_CLASS = {
    "CAPCHA_NOT_READY": ResultNotReady,
}


class RucaptchaApi(object):
    def __init__(self, api_key, task_timeout=DEFAULT_TASK_TIMEOUT):
        self.api_key = api_key
        self.pool = PoolManager()
        self.task_timeout = task_timeout

    # Parameter Check Methods

    def check_parameter_reserved(self, name, value):
        if value is not None:
            raise ConfigurationError('Parameter "{}" is not configurable'.format(name))

    def check_parameter_options(self, name, value, options):
        if value is not None and value not in options:
            raise ConfigurationError(
                'Parameter "{}"  must be one of: [{}]'.format(
                    name, ", ".join(map(str, options))
                )
            )

    def check_parameter_range(self, name, value, min_value, max_value):
        if value is not None and value < min_value or value > max_value:
            raise ConfigurationError(
                'Parameter "{}"  must be in range from {} to {}'.format(
                    name, min_value, max_value
                )
            )

    def check_parameter_type(self, name, value, param_type):
        if value is not None and not isinstance(value, param_type):
            raise ConfigurationError(
                'Parameter "{}"  must be of type %s'.format(name, param_type)
            )

    def check_parameter_maxlen(self, name, value, maxlen):
        if value is not None and len(value) > maxlen:
            raise ConfigurationError(
                'Length of parameter "{}" must not be more than {}'.format(name, maxlen)
            )

    # Internal Methods

    def build_error(self, res_data):
        error_code = res_data["request"]
        error_cls = ERROR_CLASS.get(error_code, ApiError)
        return error_cls(
            "{}|{}".format(
                res_data["request"],
                res_data.get("error_text"),
            )
        )

    def parse_response(self, res_data_bytes):
        res_data = json.loads(res_data_bytes.decode("utf-8"))
        if res_data["status"] == 1:
            return res_data["request"]
        else:
            raise self.build_error(res_data)

    # Generic Methods

    def submit_task(self, **params):
        url = "http://rucaptcha.com/in.php"
        fields = {
            "key": self.api_key,
            "json": "1",
        }
        for key, val in params.items():
            if val is not None:
                fields[key] = val
        res = self.pool.request("POST", url, fields=fields)
        return self.parse_response(res.data)

    def get_task_result(self, task_id):
        url = "http://rucaptcha.com/res.php"
        fields = {
            "key": self.api_key,
            "action": "get",
            "id": str(task_id),
            "json": "1",
        }
        res = self.pool.request("GET", url, fields=fields)
        return self.parse_response(res.data)

    def process_task(self, **task_params):
        task_id = self.submit_task(**task_params)
        return self.wait_task_result(task_id)

    def wait_task_result(self, task_id):
        start = time.time()
        while (time.time() - start) < self.task_timeout:
            try:
                return self.get_task_result(task_id)
            except ResultNotReady:
                logging.debug("Result for task id={} is not ready".format(task_id))
                time.sleep(5)
        raise ResultTimeout(
            "Timed out while waiting for result for task id={}".format(task_id)
        )

    # Image Captcha Methods

    def submit_task_image(
        self,
        file,
        key=None,
        method=None,
        body=None,
        phrase=0,
        regsense=0,
        numeric=0,
        calc=0,
        min_len=0,
        max_len=0,
        language=0,
        lang=None,
        textinstructions=None,
        imginstructions=None,
        header_acao=0,
        pingback=None,
        json=None,
        soft_id=SOFTWARE_ID,
    ):
        # reserved
        self.check_parameter_reserved("key", key)
        self.check_parameter_reserved("method", method)
        self.check_parameter_reserved("json", json)
        # positional
        if not isinstance(file, bytes):
            raise ConfigurationError('Parameter "file" must be bytes')
        # optional
        if body is not None:
            raise ConfigurationError(
                'Instead of "body" parameter pass raw image bytes in "file" parameter'
            )
        self.check_parameter_options("phrase", phrase, set([0, 1]))
        self.check_parameter_options("regsense", regsense, set([0, 1]))
        self.check_parameter_options("numeric", numeric, set([0, 1, 2, 3, 4]))
        self.check_parameter_options("calc", calc, set([0, 1]))
        self.check_parameter_range("min_len", min_len, 0, 20)
        self.check_parameter_range("max_len", max_len, 0, 20)
        self.check_parameter_options("language", language, set([0, 1, 2]))
        self.check_parameter_options("lang", lang, VALID_LANGS)
        self.check_parameter_type("textinstructions", textinstructions, str)
        self.check_parameter_maxlen("textinstructions", textinstructions, 140)
        self.check_parameter_type("imginstructions", imginstructions, bytes)
        self.check_parameter_options("header_acao", header_acao, set([0, 1]))
        self.check_parameter_type("pingback", pingback, str)
        self.check_parameter_type("soft_id", soft_id, int)
        return self.submit_task(
            body=b64encode(file),
            method="base64",
            phrase=phrase,
            regsense=regsense,
            numeric=numeric,
            calc=calc,
            min_len=min_len,
            max_len=max_len,
            language=language,
            lang=lang,
            textinstructions=textinstructions,
            imginstructions=imginstructions,
            header_acao=header_acao,
            pingback=pingback,
            soft_id=soft_id,
        )

    def process_task_image(self, file, **kwargs):
        return self.wait_task_result(self.submit_task_image(file, **kwargs))

    # Text Captcha Methods

    def submit_task_text(
        self,
        textcaptcha,
        key=None,
        language=0,
        lang=None,
        header_acao=0,
        pingback=None,
        json=None,
        soft_id=SOFTWARE_ID,
    ):
        # reserved
        self.check_parameter_reserved("key", key)
        self.check_parameter_reserved("json", json)
        # positional
        self.check_parameter_type("textcaptcha", textcaptcha, str)
        self.check_parameter_maxlen("textcaptcha", textcaptcha, 140)
        # optional
        self.check_parameter_options("language", language, set([0, 1, 2]))
        self.check_parameter_options("lang", lang, VALID_LANGS)
        self.check_parameter_options("header_acao", header_acao, set([0, 1]))
        self.check_parameter_type("pingback", pingback, str)
        self.check_parameter_type("soft_id", soft_id, int)

        return self.submit_task(
            textcaptcha=textcaptcha,
            language=language,
            lang=lang,
            header_acao=header_acao,
            pingback=pingback,
            soft_id=soft_id,
        )

    # Recaptcha V2 Captcha Methods

    def submit_task_recaptcha_v2(
        self,
        googlekey,
        pageurl,
        key=None,
        method=None,
        domain="google.com",
        invisible=0,
        data_s=None,
        cookies=None,
        useragent=None,
        header_acao=0,
        pingback=None,
        json=None,
        soft_id=SOFTWARE_ID,
        proxy=None,
        proxytype=None,
    ):
        # reserved
        self.check_parameter_reserved("key", key)
        self.check_parameter_reserved("method", key)
        self.check_parameter_reserved("json", json)
        # positional
        self.check_parameter_type("googlekey", googlekey, str)
        self.check_parameter_type("pageurl", pageurl, str)
        # optional
        self.check_parameter_options(
            "domain", domain, set(["google.com", "recaptcha.net"])
        )
        self.check_parameter_options("invisible", invisible, set([0, 1]))
        self.check_parameter_type("data_s", data_s, str)
        self.check_parameter_type("cookies", cookies, str)
        self.check_parameter_type("useragent", useragent, str)
        self.check_parameter_options("header_acao", header_acao, set([0, 1]))
        self.check_parameter_type("pingback", pingback, str)
        self.check_parameter_type("soft_id", soft_id, int)
        self.check_parameter_type("proxy", proxy, str)
        self.check_parameter_type("proxytype", proxytype, str)
        if proxytype:
            proxytype = proxytype.upper()
            self.check_parameter_options(
                "proxytype", proxytype, set(["HTTP", "HTTPS", "SOCKS4", "SOCKS5"])
            )

        return self.submit_task(
            googlekey=googlekey,
            pageurl=pageurl,
            method="userrecaptcha",
            domain=domain,
            invisible=invisible,
            data_s=data_s,
            cookies=cookies,
            useragent=useragent,
            header_acao=header_acao,
            pingback=pingback,
            soft_id=soft_id,
            proxy=proxy,
            proxytype=proxytype,
        )

    def process_task_recaptcha_v2(self, textcaptcha, **kwargs):
        return self.wait_task_result(
            self.submit_task_recaptcha_v2(textcaptcha, **kwargs)
        )

    # Recaptcha V3 Captcha Methods

    def submit_task_recaptcha_v3(
        self,
        googlekey,
        pageurl,
        key=None,
        method=None,
        version=None,
        domain="google.com",
        action="verify",
        min_score=0.4,
        header_acao=0,
        pingback=None,
        json=None,
        soft_id=SOFTWARE_ID,
    ):
        # reserved
        self.check_parameter_reserved("key", key)
        self.check_parameter_reserved("method", key)
        self.check_parameter_reserved("version", key)
        self.check_parameter_reserved("json", json)
        # positional
        self.check_parameter_type("googlekey", googlekey, str)
        self.check_parameter_type("pageurl", pageurl, str)
        # optional
        self.check_parameter_options(
            "domain", domain, set(["google.com", "recaptcha.net"])
        )
        self.check_parameter_type("action", action, str)
        self.check_parameter_type("min_score", min_score, float)
        self.check_parameter_options("header_acao", header_acao, set([0, 1]))
        self.check_parameter_type("pingback", pingback, str)
        self.check_parameter_type("soft_id", soft_id, int)

        return self.submit_task(
            googlekey=googlekey,
            pageurl=pageurl,
            method="userrecaptcha",
            version="v3",
            domain=domain,
            action=action,
            min_score=min_score,
            header_acao=header_acao,
            pingback=pingback,
            soft_id=soft_id,
        )

    def process_task_recaptcha_v3(self, textcaptcha, **kwargs):
        return self.wait_task_result(
            self.submit_task_recaptcha_v3(textcaptcha, **kwargs)
        )

    # Recaptcha Enterprise Captcha Methods

    def submit_task_recaptcha_enterprise(
        self,
        googlekey,
        pageurl,
        key=None,
        method=None,
        version=None,
        domain="google.com",
        action="verify",
        min_score=0.4,
        header_acao=0,
        pingback=None,
        json=None,
        soft_id=SOFTWARE_ID,
        proxy=None,
        proxytype=None,
    ):
        # reserved
        self.check_parameter_reserved("key", key)
        self.check_parameter_reserved("method", key)
        self.check_parameter_reserved("version", key)
        self.check_parameter_reserved("json", json)
        # positional
        self.check_parameter_type("googlekey", googlekey, str)
        self.check_parameter_type("pageurl", pageurl, str)
        # optional
        self.check_parameter_options(
            "domain", domain, set(["google.com", "recaptcha.net"])
        )
        self.check_parameter_type("action", action, str)
        self.check_parameter_type("min_score", min_score, float)
        self.check_parameter_options("header_acao", header_acao, set([0, 1]))
        self.check_parameter_type("pingback", pingback, str)
        self.check_parameter_type("soft_id", soft_id, int)
        self.check_parameter_type("proxy", proxy, str)
        self.check_parameter_type("proxytype", proxytype, str)
        if proxytype:
            proxytype = proxytype.upper()
            self.check_parameter_options(
                "proxytype", proxytype, set(["HTTP", "HTTPS", "SOCKS4", "SOCKS5"])
            )

        return self.submit_task(
            googlekey=googlekey,
            pageurl=pageurl,
            method="userrecaptcha",
            version="enterprise",
            domain=domain,
            action=action,
            min_score=min_score,
            header_acao=header_acao,
            pingback=pingback,
            soft_id=soft_id,
            proxy=proxy,
            proxytype=proxytype,
        )

    def process_task_recaptcha_enterprise(self, textcaptcha, **kwargs):
        return self.wait_task_result(
            self.submit_task_recaptcha_enterprise(textcaptcha, **kwargs)
        )
