import math
from shutil import disk_usage
from django.utils.translation import gettext as _
from django.urls.base import reverse
from django.conf import settings
from django.utils.timezone import now
from django.contrib.sites.shortcuts import get_current_site
from apps.catalogue.models import Product, ProductImage
from delivery.models import Postcode
from custom.views import DynamicDataView
from pages.models import Page, Category


TIMESTAMP = settings.TIMESTAMP


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def get_delivery_possibility(request):
    if request.user.is_authenticated and request.user.delivered_addresses:
        return 'possible'
    elif 'postcode' in request.session:
        postcode = request.GET.get('postcode', request.session.get('postcode'))
        if int(postcode) in Postcode.get_all_postcodes():
            return 'possible_manual'
        else:
            return 'impossible'
    else:
        return 'unknown'


def get_progress_from_timestamp(datetime_after, datetime_until):
    difference = datetime_until.timestamp() - datetime_after.timestamp()
    if not difference:
        return 0
    elapsed = now().timestamp() - datetime_after.timestamp()
    progress = int(elapsed / difference * 100)
    if progress < 0:
        progress = 0
    elif progress > 100:
        progress = 100
    return progress


def main(request, *args, **kwargs):
    context = {}
    context.update({
        'CONFIG': get_current_site(request).configuration,
        'STAGE': settings.STAGE,
        'delivery_possibility': get_delivery_possibility(request),
        'message_ajax_url': reverse('message-ajax-url'),
        'lockdown_after': getattr(settings, 'LOCKDOWN_AFTER', None),
        'lockdown_until': getattr(settings, 'LOCKDOWN_UNTIL', None),
        'now': now(),
        'pages': {
            'company': Page.objects.filter(category=Category.COMPANY),
            'legal': Page.objects.filter(category=Category.LEGAL),
        },
        'hide_price': request.user.hide_price,
    })
    if context['lockdown_after'] and context['lockdown_until']:
        context['lockdown_progress_pct'] = get_progress_from_timestamp(
            settings.LOCKDOWN_AFTER, settings.LOCKDOWN_UNTIL
        )
    statistic_ctx = {}
    if request.user.is_staff:
        statistic_ctx[_('Start Time')] = TIMESTAMP
        statistic_ctx[_('Free Space')] = convert_size(disk_usage(__file__).free)
        statistic_ctx[_('Offered Products')] = Product.objects.filter(is_public=True).count()
        statistic_ctx[_('Images')] = ProductImage.objects.count()
    return {'statistic': statistic_ctx, **context}
