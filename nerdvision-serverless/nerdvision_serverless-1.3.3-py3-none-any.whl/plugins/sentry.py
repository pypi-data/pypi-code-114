from nerdvision.plugins import Plugin, DidNotEnable

try:
    from sentry_sdk import Client  # type: ignore
except ImportError:
    raise DidNotEnable("sentry_sdk is not installed")


class SentryErrorPlugin(Plugin):

    def load_plugin(self, nerdvision):
        old_sen_capture = Client.capture_event

        def nv_capture(self, event, hint=None, scope=None):
            if hint is not None:
                exc_info = hint.get('exc_info')
                if exc_info:
                    nerdvision.capture_exception(exc_info)

            old_sen_capture(self, event, hint, scope)

        Client.capture_event = nv_capture
