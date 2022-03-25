from django.contrib import admin

from .models import Empfaenger

class EmpfaengerAdmin(admin.ModelAdmin):
    model = Empfaenger
    fields = [
        'name',
        'email',
        'required',
    ]
    list_display = (
        'name',
        'email',
        'required',
    )
    search_fields = [
        'name',
        'email',
    ]
    list_filter = [
        'name',
        'email',
    ]

admin.site.register(Empfaenger, EmpfaengerAdmin)
