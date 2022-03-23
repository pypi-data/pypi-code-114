from django.contrib import admin
from .models import *
import hashlib

from import_export import resources

from import_export.admin import ImportExportModelAdmin



class CitizenResource(resources.ModelResource):
    class Meta:
        model = Citizen
class CitizenAdmin(ImportExportModelAdmin):
    resource_class = CitizenResource
admin.site.register(Citizen, CitizenAdmin)


class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language
class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource
admin.site.register(Language, LanguageAdmin)



class FamilyCardOnlineResource(resources.ModelResource):
    class Meta:
        model = FamilyCardOnline
class FamilyCardOnlineAdmin(ImportExportModelAdmin):
    resource_class = FamilyCardOnlineResource
admin.site.register(FamilyCardOnline, FamilyCardOnlineAdmin)


class PopulationResource(resources.ModelResource):
    class Meta:
        model = Population
class PopulationAdmin(ImportExportModelAdmin):
    resource_class = PopulationResource
admin.site.register(Population, PopulationAdmin)



class DeficientResource(resources.ModelResource):
    class Meta:
        model = Deficient
class DeficientAdmin(ImportExportModelAdmin):
    resource_class = DeficientResource
admin.site.register(Deficient, DeficientAdmin)




class ProfessionResource(resources.ModelResource):
    class Meta:
        model = Profession
class ProfessionAdmin(ImportExportModelAdmin):
    resource_class = ProfessionResource
admin.site.register(Profession, ProfessionAdmin)


class ReligionResource(resources.ModelResource):
    class Meta:
        model = Religion
class ReligionAdmin(ImportExportModelAdmin):
    resource_class = ReligionResource
admin.site.register(Religion, ReligionAdmin)


class DetailFamilyResource(resources.ModelResource):
    class Meta:
        model = DetailFamily
class DetailFamilyAdmin(ImportExportModelAdmin):
    resource_class = DetailFamilyResource
admin.site.register(DetailFamily, DetailFamilyAdmin)


class FamilyResource(resources.ModelResource):
    class Meta:
        model = Family
class FamilyAdmin(ImportExportModelAdmin):
    resource_class = FamilyResource
admin.site.register(Family, FamilyAdmin)




class FamilyPositionResource(resources.ModelResource):
    class Meta:
        model = FamilyPosition
class FamilyPositionAdmin(ImportExportModelAdmin):
    resource_class =FamilyPositionResource
admin.site.register(FamilyPosition, FamilyPositionAdmin)



class Level_EducationResource(resources.ModelResource):
    class Meta:
        model = Level_Education
class Level_EducationAdmin(ImportExportModelAdmin):
    resource_class =Level_EducationResource
admin.site.register(Level_Education,Level_EducationAdmin)


class TemporaryResource(resources.ModelResource):
    class Meta:
        model = Temporary
class TemporaryAdmin(ImportExportModelAdmin):
    resource_class =TemporaryResource
admin.site.register(Temporary,TemporaryAdmin)



class MigrationResource(resources.ModelResource):
    class Meta:
        model = Migration
class MigrationAdmin(ImportExportModelAdmin):
    resource_class =MigrationResource
admin.site.register(Migration,MigrationAdmin)


class MigrationoutResource(resources.ModelResource):
    class Meta:
        model = Migrationout
class MigrationoutAdmin(ImportExportModelAdmin):
    resource_class = MigrationoutResource
admin.site.register(Migrationout,MigrationoutAdmin)


class ChangeFamilyResource(resources.ModelResource):
    class Meta:
        model = ChangeFamily
class ChangeFamilyAdmin(ImportExportModelAdmin):
    resource_class = ChangeFamilyResource
admin.site.register(ChangeFamily,ChangeFamilyAdmin)



class DeathResource(resources.ModelResource):
    class Meta:
        model = Death
class DeathAdmin(ImportExportModelAdmin):
    resource_class = DeathResource
admin.site.register(Death,DeathAdmin)