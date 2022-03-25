import io
import json
from zipfile import ZipFile
from django.urls.base import reverse
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.http.response import FileResponse, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from oscar.apps.dashboard.offers import views
from newsletter.generator.forms import MessageGeneratorForm
from apps.offer.models import ConditionalOffer, RangeProduct, Range
from apps.offer.utils import InkscapeConverter, default_inkscape_template, \
    subtitled_inkscape_template
from .forms import OfferRangeProductForm

__all__ = ('ProductOfferListView', 'ProductOfferDetailView',
           'ProductOfferCreateView', 'ProductOfferUpdateView',
           'ProductOfferDeleteView', 'ProductOfferFormView')


class SlideView(View):
    """ Most of this is in utils.InkscapeConverter also the renderer """
    http_method_names = ['get']

    def get(self, request, range_product_pk, suffix, *args, **kwargs):
        range_product = RangeProduct.objects.get(id=range_product_pk)
        converter = InkscapeConverter(range_product, suffix)
        return FileResponse(converter.file, filename=converter.filename)


class SlideViewPreview(View):
    http_method_names = ['post']
    form_class = OfferRangeProductForm

    def post(self, request, range_pk, *args, **kwargs):
        form = self.form_class(Range.objects.get(pk=range_pk), request.POST)
        if form.is_valid() and form.cleaned_data['image']:
            converter = InkscapeConverter(form.instance, 'png', width=800)
            return HttpResponse(f'data:image/jpg;base64,{converter.base64}')
        return HttpResponse('')


class ZippedSlidesView(View):
    http_method_names = ['get']

    def get(self, request, offer_pk, *args, **kwargs):
        offer = ConditionalOffer.objects.get(pk=offer_pk)
        qs = RangeProduct.objects.filter(
            range=offer.benefit.range,
            cached_slide__isnull=False,
        ).exclude(cached_slide='')

        zip_file = io.BytesIO()
        with ZipFile(zip_file, 'w') as file:
            index = 0
            for range_product in qs:
                index += 1
                title = range_product.get_title().replace('<br>', ' ')
                cached_file = range_product.cached_slide.file.read()
                file.writestr(
                    f'{index:02d}_{range_product.pk}_{title}.png',
                    cached_file,
                )
        return HttpResponse(zip_file.getvalue(), content_type='application/zip')


class MessageGeneratorMixin:
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['message_generator_form'] = MessageGeneratorForm(self.request)
        return context


class OfferWizardStepView(views.OfferWizardStepView):
    def _store_form_kwargs(self, form):
        session_data = self.request.session.setdefault(self.wizard_name, {})

        # Adjust kwargs to avoid trying to save the range instance
        form_data = form.cleaned_data.copy()
        product_range = form_data.get('range')
        if product_range is not None:
            form_data['range'] = product_range.id

        combinations = form_data.get('combinations')
        if combinations is not None:
            form_data['combination_ids'] = [x.id for x in combinations]
            del form_data['combinations']

        if 'partner' in form_data and form_data['partner']:
            form_data['partner'] = form_data['partner'].pk

        form_kwargs = {'data': form_data}
        json_data = json.dumps(form_kwargs, cls=DjangoJSONEncoder)

        session_data[self._key()] = json_data
        self.request.session.save()

    def save_offer(self, offer):
        session_offer = self._fetch_session_offer()
        offer.partner = session_offer.partner
        result = views.OfferWizardStepView.save_offer(self, offer)
        return result


class OfferMetaDataView(OfferWizardStepView, views.OfferMetaDataView):
    """ Partner is serialized """


class OfferRestrictionsView(OfferWizardStepView, views.OfferRestrictionsView):
    """ Partner is deserialized when saving """


class OfferDetailView(MessageGeneratorMixin, views.OfferDetailView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        offer = ctx.get('offer')
        if offer and offer.benefit and offer.benefit.range:
            range = offer.benefit.range  # @ReservedAssignment
            ctx['range'] = range
            ctx['range_products'] = range.rangeproduct_set.all()
            ctx['slides'] = RangeProduct.objects.filter(
                image__isnull=False,
                range=range,
            )
        return ctx


class OfferRangeProductMixin:
    model = RangeProduct
    form_class = OfferRangeProductForm

    def get_conditional_offer(self):
        return ConditionalOffer.objects.get(
            pk=self.kwargs['offer_pk'])

    def get_range(self):
        return self.get_conditional_offer().benefit.range

    def get_range_product(self):
        """ For Single Object Use """
        return RangeProduct.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['offer'] = self.get_conditional_offer()
        ctx['width_ratio'] = default_inkscape_template.width_ratio
        ctx['height_ratio'] = default_inkscape_template.height_ratio
        ctx['subtitled_width_ratio'] = subtitled_inkscape_template.width_ratio
        ctx['subtitled_height_ratio'] = subtitled_inkscape_template.height_ratio
        return ctx

    def get_success_url(self):
        nxt = self.request.GET.get('next')
        if nxt:
            return nxt
        kwargs = {'offer_pk': self.kwargs['offer_pk']}
        return reverse('dashboard:product-offer-list', kwargs=kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['range'] = self.get_range()
        return kwargs


class OfferRangeProductListView(MessageGeneratorMixin, OfferRangeProductMixin,
                                ListView):
    template_name = 'oscar/dashboard/offers/product_offer_list.html'

    def get_queryset(self):
        qs = ListView.get_queryset(self)
        qs = qs.filter(range=self.get_conditional_offer().benefit.range)
        qs = qs.order_by('-display_order')
        return qs


class OfferRangeProductUpdateView(OfferRangeProductMixin, UpdateView):
    template_name = 'oscar/dashboard/offers/product_offer_update.html'


class OfferRangeProductCreateView(OfferRangeProductMixin, CreateView):
    template_name = 'oscar/dashboard/offers/product_offer_update.html'


class OfferRangeProductDeleteView(OfferRangeProductMixin, DeleteView):
    template_name = 'oscar/dashboard/offers/product_offer_delete.html'
