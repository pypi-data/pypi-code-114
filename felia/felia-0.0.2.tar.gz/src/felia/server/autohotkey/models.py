from django.db import models

from server.autohotkey import constant

# Create your models here.


class Script(models.Model):
    class ModeInAHK(models.TextChoices):
        INCLUDE = 'ic', constant.Mode_Include
        SWITCH = 'sw', constant.Mode_Switch

    file = models.CharField(max_length=20)
    mode = models.CharField(max_length=2, choices=ModeInAHK.choices)
    help_text = models.TextField(help_text="热键说明", null=True, blank=True)


class HotKey(models.Model):
    key = models.CharField(max_length=10, help_text="热键")
    action = models.TextField(help_text="动作")
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    help_text = models.TextField(help_text="热键说明", null=True, blank=True)
