from django.db import models

from simpel.simpel_core import const
from simpel.simpel_core.abstracts import BaseManager, ParanoidPolymorphicManager


class OrderManager(ParanoidPolymorphicManager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related("items")

    def get_stats(self, **kwargs):
        qs = self.get_queryset().select_related("final_document")
        if kwargs:
            qs = qs.filter(**kwargs)
        qs = qs.annotate(
            processing_response=models.F("date_processed") - models.F("date_validated"),
            completion_response=models.F("date_completed") - models.F("date_processed"),
            invoicing_response=models.F("date_invoiced") - models.F("date_completed"),
            closing_response=models.F("date_closed") - models.F("date_invoiced"),
            execution_response=models.F("date_closed") - models.F("date_validated"),
        )
        return qs

    def get_stats_by_services(self):
        qs = self.get_stats()
        qs = (
            qs.values("group")
            .annotate(
                # Total Values
                pending_total=models.Sum("grand_total", filter=models.Q(status=const.PENDING)),
                valid_total=models.Sum("grand_total", filter=models.Q(status=const.VALID)),
                processed_total=models.Sum("grand_total", filter=models.Q(status=const.PROCESSED)),
                complete_total=models.Sum("grand_total", filter=models.Q(status=const.COMPLETE)),
                invoiced_total=models.Sum("grand_total", filter=models.Q(status=const.INVOICED)),
                closed_total=models.Sum("grand_total", filter=models.Q(status=const.CLOSED)),
                all_total=models.Sum("grand_total"),
                # Count Values
                pending_count=models.Count("group", filter=models.Q(status=const.PENDING)),
                valid_count=models.Count("group", filter=models.Q(status=const.VALID)),
                processed_count=models.Count("group", filter=models.Q(status=const.PROCESSED)),
                complete_count=models.Count("group", filter=models.Q(status=const.COMPLETE)),
                invoiced_count=models.Count("group", filter=models.Q(status=const.INVOICED)),
                closed_count=models.Count("group", filter=models.Q(status=const.CLOSED)),
                all_count=models.Count("group"),
                sampling_count=models.Count("group", filter=models.Q(sampling=True)),
                # Response Time
                processing_response_avg=models.Avg("processing_response"),
                completion_response_avg=models.Avg("completion_response"),
                invoicing_response_avg=models.Avg("invoicing_response"),
                closing_response_avg=models.Avg("closing_response"),
                execution_response_avg=models.Avg("execution_response"),
            )
            .order_by()
        )
        return qs


class OrderItemManager(BaseManager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("product").prefetch_related("bundles")


class OrderItemBundleManager(BaseManager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("product")
