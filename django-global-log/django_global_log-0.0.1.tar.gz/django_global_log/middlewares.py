import logging
import sys
import traceback
from timeit import default_timer as timer

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils.module_loading import import_string

from django_global_log.serializers import LogSaveSerializer
from django_global_log.utils import get_ip

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
            "path": request.path,
            "detail": {
                "full_url": request.build_absolute_uri(),
                "params": request.GET,
                "resp_size": sys.getsizeof(response.content),
                "req_header": dict(request.headers),
            },
            "code": response.status_code,
            "duration": duration,
            "ip": get_ip(request),
        }
        self.save_log(log_detail)

    def save_log(self, detail):
        serializer = LogSaveSerializer(data=detail)
        serializer.is_valid(raise_exception=True)
        celery_log_func_string = getattr(settings, "GLOBAL_LOG_CELERY_FUNC", None)
        if celery_log_func_string is None:
            serializer.save()
        else:
            try:
                celery_log_func = import_string(celery_log_func_string)
                celery_log_func.delay(serializer.data)
            except ImportError:
                logger.error("[Celery Log Func Not Exists] %s", celery_log_func_string)
                serializer.save()
