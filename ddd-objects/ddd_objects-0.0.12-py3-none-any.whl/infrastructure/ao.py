import traceback

from ..domain.value_obj import AOResult

def exception_helper(max_try=3):
    def _exception_helper(func):
        def _f(*args, **kwargs):
            for _ in range(max_try):
                try:
                    return AOResult(func(*args, **kwargs))
                except:
                    error_info = traceback.format_exc()
            else:
                return AOResult(error_info=error_info)
        return _f
    return _exception_helper