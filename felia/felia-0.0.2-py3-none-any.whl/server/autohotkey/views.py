import os
from importlib import import_module

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.conf import settings

from server.autohotkey.registry import files

from .models import Script
# Create your views here.


class HotKeyListView(ListView):
    model = Script
    template_name = 'ahk/hotkey_list.html'


def call_python(request):
    func = request.GET.get("func")
    if func is None:
        return HttpResponse("未提供func参数!")
    files.all_funcs[func](request)

    return HttpResponse("OK")


for module in os.listdir(settings.BASE_DIR / 'autohotkey' / 'scripts'):
    name, t = os.path.splitext(module)
    if name.startswith("__") or t != '.py':
        continue
    import_module(f'server.autohotkey.scripts.{name}')