import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from base.decorators import ajax_required
from .models import Customer
from .validate import validate_webhook_request


@require_POST
@ajax_required
def get_paddle_info(request):
    response = {}
    response["vendor_id"] = settings.PADDLE_VENDOR_ID
    response["monthly_plan_id"] = settings.PADDLE_MONTHLY_PLAN_ID
    response["six_months_plan_id"] = settings.PADDLE_SIX_MONTHS_PLAN_ID
    response["annual_plan_id"] = settings.PADDLE_ANNUAL_PLAN_ID
    return JsonResponse(response, status=200)


@login_required
@require_POST
@ajax_required
def get_subscription_details(request):
    response = {}
    response["staff"] = request.user.is_staff
    customer = Customer.objects.filter(user=request.user).first()
    if customer:
        if (
            customer.cancelation_date is None
            or customer.cancelation_date > datetime.date.today()
        ):
            response["subscribed"] = customer.subscription_type
            response["status"] = customer.status
            response["cancel_url"] = customer.cancel_url
            response["update_url"] = customer.update_url
            if customer.cancelation_date:
                response["subscription_end"] = customer.cancelation_date
        else:
            response["subscribed"] = False
            customer.delete()
    else:
        response["subscribed"] = False
    return JsonResponse(response, status=200)


@csrf_exempt
@require_POST
def webhook(request):
    status = 200
    if not validate_webhook_request(request.POST):
        status = 403
        return JsonResponse({}, status=status)
    alert_name = request.POST["alert_name"]
    if alert_name not in [
        "subscription_created",
        "subscription_updated",
        "subscription_cancelled",
    ]:
        return JsonResponse({}, status=status)
    user_id = int(request.POST["passthrough"])
    user = User.objects.filter(id=user_id).first()
    if not user:
        return JsonResponse({}, status=status)
    subscription_plan_id = int(request.POST["subscription_plan_id"])
    if int(subscription_plan_id) not in [
        settings.PADDLE_MONTHLY_PLAN_ID,
        settings.PADDLE_SIX_MONTHS_PLAN_ID,
        settings.PADDLE_ANNUAL_PLAN_ID,
    ]:
        return JsonResponse({}, status=status)
    if alert_name == "subscription_created":
        # Delete old customers, if any
        Customer.objects.filter(user=user).delete()
        # Then create a new customer
        customer = Customer(
            user=user, subscription_id=request.POST["subscription_id"]
        )
    else:
        customer = Customer.objects.filter(
            user=user, subscription_id=request.POST["subscription_id"]
        ).first()
        if not customer:
            return JsonResponse({}, status=status)
    customer.status = request.POST["status"]
    if alert_name == "subscription_updated":
        customer.unit_price = request.POST["new_unit_price"]
    else:
        customer.unit_price = request.POST["unit_price"]
    customer.currency = request.POST["currency"]
    customer.subscription_plan_id = request.POST["subscription_plan_id"]
    if alert_name == "subscription_cancelled":
        customer.cancelation_date = request.POST["cancellation_effective_date"]
    else:
        customer.cancel_url = request.POST["cancel_url"]
        customer.update_url = request.POST["update_url"]
    if int(customer.subscription_plan_id) == settings.PADDLE_ANNUAL_PLAN_ID:
        customer.subscription_type = "annual"
    elif (
        int(customer.subscription_plan_id)
        == settings.PADDLE_SIX_MONTHS_PLAN_ID
    ):
        customer.subscription_type = "sixmonths"
    else:
        customer.subscription_type = "monthly"
    customer.save()

    return JsonResponse({}, status=status)
