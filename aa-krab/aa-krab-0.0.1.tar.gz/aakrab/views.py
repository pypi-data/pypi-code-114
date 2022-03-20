from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from allianceauth.authentication.models import CharacterOwnership
from utils import logger



@login_required()
@permission_required("aakrab.basic_access")
def index(request):
    """
    index
    :param request:
    :return:
    """

    msg = None

    if "msg" in request.session:
        msg = request.session.pop("msg")

    chars = CharacterOwnership.objects.filter(user=request.user)
    fats = []

    context = {
        "chars": chars,
        "msg": msg,
    }

    logger.info("Module called by %s", request.user)

    return render(request, "aa-krab/index.html", context)

