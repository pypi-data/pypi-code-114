from django_hookup import core as hookup

from .models import CalibrationService, CalibrationTask


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_simpel_calibration_initial_perms():
    from .apps import init_permissions

    init_permissions()


@hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
def register_calibration_service_model():
    return CalibrationService


@hookup.register("REGISTER_TASK_CHILD_MODELS")
def register_calibration_task():
    return CalibrationTask
