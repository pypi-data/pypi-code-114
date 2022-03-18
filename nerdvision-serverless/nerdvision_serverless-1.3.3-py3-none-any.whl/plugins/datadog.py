from datetime import datetime

from nerdvision.plugins import Plugin, DidNotEnable

try:
    from ddtrace import Span, tracer  # type: ignore
except ImportError as e:
    raise DidNotEnable("ddtrace is not installed", e)


class DatadogAPMPlugin(Plugin):
    def load_plugin(self, nerdvision):
        old_set_exc_info = Span.set_exc_info

        def wrapped_set_exc_info(self, exc_type, exc_val, exc_tb):
            nerdvision.capture_exception(exc_type, exc_val, exc_tb)
            return old_set_exc_info(self, exc_type, exc_val, exc_tb)

        Span.set_exc_info = wrapped_set_exc_info

        def nv_dd_decorator(data):
            span = tracer.current_span()
            if span is not None:
                span.set_tag('nerdvision.link', 'https://app.nerd.vision/context/%s' % data['id'])
                data['tags']['span_id'] = "%s" % span.context.span_id
                data['tags']['trace_id'] = "%s" % span.context.trace_id
                data['tags']['trace_service'] = "%s" % span.service
                data['tags']['trace_name'] = "%s" % span.name
                data['tags']['trace_resource'] = "%s" % span.resource
                return 'dd_trace', {
                    'id': 'dd_trace',
                    'service': span.service,
                    'name': span.name,
                    'span_id': "%s" % span.context.span_id,
                    'trace_id': "%s" % span.context.trace_id,
                    'parent_id': "%s" % span.parent_id,
                    'resource': span.resource,
                    'meta': span.meta,
                    'start_ns': datetime.fromtimestamp(span.start_ns / 1e9).strftime('%Y-%b-%d %H:%M:%S.%f')
                }
            return None

        nerdvision.add_context_decorator(nv_dd_decorator)
