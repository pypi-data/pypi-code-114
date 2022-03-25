from django import template

register = template.Library()


class Counter(object):
    def __init__(self, start=1):
        self.start = start

    def __call__(self):
        self.start += 1
        return self.start - 1


@register.simple_tag
def create_counter(start=1):
    """
    Create a counter in Template using:
    {% create_counter start=1 as counter %}

    Every time the counter is accessed, it will iterate by 1

    If you need to use one counter step multiple times, use:
    {% with counter_step=counter %}
        {{ counter_step }}
    {% endwith %}
    """
    return Counter(start)
