import logging
import sys
import traceback
from timeit import default_timer as timer

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils.module_loading import import_string

from django_global_log.serializers import LogSaveSerializer
from django_global_log.utils import SaveLogHandler, get_ip

logger = logging.getLogger("django")


class DjangoGlobalLogMiddleware(MiddlewareMixin):
    """全局日志中间件"""

    req_start_time_key = "_global_log_req_start_time"

    def process_request(self, request):
        setattr(request, self.req_start_time_key, timer())
        return None

    def process_response(self, request, response):
        try:
            self.log(request, response)
            logger.info("[DB Logging Success]")
        except Exception as err:
            msg = traceback.format_exc()
            logger.error("[DB Logging Failed] %s\n%s", str(err), msg)
        return response

    def log(self, request, response):
        req_end_time = timer()
        req_start_time = getattr(request, self.req_start_time_key, req_end_time)
        duration = int((req_end_time - req_start_time) * 1000)
        log_detail = {
            "operator": getattr(request.user, "pk", ""),
            "method": request.method,
            "path": request.path,
            "detail": {
                "full_url": request.build_absolute_uri(),
                "params": request.GET,
                "resp_size": sys.getsizeof(response.content),
                "req_header": dict(request.headers),
                **self.build_extras(request, response),
            },
            "code": response.status_code,
            "duration": duration,
            "ip": get_ip(request),
        }
        data = self._validate_data(log_detail)
        self.save(data)

    def _validate_data(self, detail):
        serializer = LogSaveSerializer(data=detail)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def build_extras(self, request, response):
        extra_func = getattr(settings, "GLOBAL_LOG_EXTRA_FUNC", {})
        extras = {}
        for key, func_string in extra_func.items():
            try:
                func = import_string(func_string)
                extras[key] = func(request, response)()
            except ImportError:
                logger.error("[Extra Log Func Not Exists] %s", func_string)
            except Exception as err:
                msg = traceback.format_exc()
                logger.error(
                    "[Extra Log Build Error] %s\t%s\n%s", func_string, err, msg
                )
        return extras

    def save(self, detail):
        custom_save_func_string = getattr(settings, "GLOBAL_LOG_SAVE_FUNC", None)
        custom_save_func_using_celery = getattr(
            settings, "GLOBAL_LOG_USING_CELERY", False
        )
        if custom_save_func_string is None:
            self._save(detail)
        else:
            try:
                custom_save_func = import_string(custom_save_func_string)
                if custom_save_func_using_celery:
                    custom_save_func.delay(detail)
                else:
                    custom_save_func(detail)
            except Exception as err:
                msg = traceback.format_exc()
                logger.error(
                    "[Custom Log Save Func Error] %s\t%s\n%s",
                    custom_save_func_string,
                    err,
                    msg,
                )
                self._save(detail)

    def _save(self, detail):
        celery_log_func_string = getattr(settings, "GLOBAL_LOG_CELERY_FUNC", None)
        if celery_log_func_string is None:
            SaveLogHandler(detail)()
        else:
            try:
                celery_log_func = import_string(celery_log_func_string)
                celery_log_func.delay(detail)
            except ImportError:
                logger.error("[Celery Log Func Not Exists] %s", celery_log_func_string)
                SaveLogHandler(detail)()
