import factory as fc

from simpel.simpel_products.tests.factories import ServiceFactory

from ..models import CalibrationService


class CalibrationServiceFactory(ServiceFactory):
    name = fc.Sequence(lambda n: f"Calibration {n}")
    analysis_method = "ISO-TEST-0001"

    class Meta:
        model = CalibrationService
        django_get_or_create = ("name",)
