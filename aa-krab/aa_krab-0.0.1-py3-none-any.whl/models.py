from django.db import models

class KrabFleet(models.Model):

    class Meta():
        default_permissions = (())
        permissions = (('basic_access', 'Can access the krab fleet module.'),)

