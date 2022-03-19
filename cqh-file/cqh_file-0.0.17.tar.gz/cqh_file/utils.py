import hashlib
import base64
def get_md5(file_path):
    h = hashlib.md5()
    h.update(open(file_path, 'rb').read())

    return h.hexdigest()


def get_base64(file_path):
    return base64.b64encode(open(file_path, 'rb').read()).decode("utf-8")

def request_with_retry(fn_get_response, session=None, max_request_count=10, error_predict=None, logger=None):
    import tenacity
    from urllib3.exceptions import ProtocolError
    # urllib3.exceptions.ProtocolError
    import requests

    def after_hook(retry_state):
        if session is not None:
            if retry_state.outcome.failed:
                state_exception = retry_state.outcome.exception()
                # requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
                if isinstance(state_exception, (ProtocolError, requests.exceptions.ConnectionError)):
                    if logger is not None:
                        logger.info("request with retry session close")
                    session.close()

    def default_error_predict(result):
        status_code = result.status_code
        if status_code != 200:
            return True
        return False

    error_predict = error_predict or default_error_predict
    return tenacity.retry(stop=tenacity.stop_after_attempt(max_request_count),
                          wait=tenacity.wait_fixed(0.9),
                          retry=tenacity.retry_if_exception_type((requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout,
                                                                  ProtocolError)) | tenacity.retry_if_result(default_error_predict),
                          after=after_hook,
                          reraise=True)(fn_get_response)()
