from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from employee.models import *
from population.models import Population, DetailFamily, Family, Religion, Profession, Citizen, Aldeia, Village, User, Migration, Death, Migrationout, Temporary
from django.utils import timezone
from django.contrib.auth.views import LoginView

from .forms import CustomAuthenticationForm

from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from population.utils import createnewid
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import date
from django.http import JsonResponse
from employee.models import *

from administration.admin import *
from development.admin import *
from custom_development.admin import *



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required
from main.decorators import *

import io
from django.http import HttpResponse
from io import StringIO
import csv
import pandas as pd
import zipfile


from io import StringIO

# from pandas.compat import StringIO


# from efamily.models import *


from population.admin import *
import pandas as pd
import zipfile
from employee.admin import *





@login_required
def dashboard(request):

    family_list = Family.objects.filter(village="1")

    tinan = timezone.now().strftime("%Y")
    moris = DetailFamily.objects.filter(
        Q(population__date_of_bird__year=tinan) & Q(population__type_data='f')).count()
    mate = Death.objects.filter(Q(date__year=tinan) & Q(
        population__status_datap='ma')).count()
    muda_sai = Migrationout.objects.filter(
        Q(population__date_created__year=tinan) & Q(population__status_datap='mu')).count()
    muda_tama = DetailFamily.objects.filter(
        Q(population__date_created__year=tinan) & Q(population__type_data='m')).count()
    temporario = Temporary.objects.filter(
        Q(population__date_created__year=tinan) & Q(population__type_data='te')).count()
    permanente = Population.objects.filter(
        Q(date_created__year=tinan) & Q(status_datap='ac')).count()
    group = request.user.groups.all()[0].name
    employee = None
    if group == 'xefe' or group == 'sec':
        user = request.user
        empuser = EmployeeUser.objects.get(user=user)
        employee = Employee.objects.get(pk=empuser.employee.pk)
    context = {
        'title': 'Dashboard',
        'family_list': family_list,
        'tinan': tinan,
        'moris': moris,
        'mate': mate,
        'muda_sai': muda_sai,
        'muda_tama': muda_tama,
        'temporario': temporario,
        'group': group,
        'permanente':  permanente,
        'template': "dashboard",
        'objects': employee
    }
    return render(request, 'main/dashboard.html', context)


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm



def ExportData(request):
    context = {
    "naranfile" : "mamuk",
    }
    return render(request, 'main/export/export.html',context)


def ExportDadusSuku(request):

    
    dataagora = timezone.now()
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    naran_file =  str(userAddress.employee.municipality) + "_" + str(userAddress.employee.administrativepost) + "_" + str(userAddress.employee.village) + ".zip"
 


    dataset1 = PopulationResource().export()
    dataset2 = DetailFamilyResource().export()
    dataset3 = FamilyResource().export()
    dataset4 = TemporaryResource().export()
    dataset5 = MigrationResource().export()
    dataset6 = MigrationoutResource().export()
    dataset7 = ChangeFamilyResource().export()
    dataset8 = DeathResource().export()

    dataset9 = PositionResource().export()
    dataset10 = MandatePeriodResource().export()
    dataset11 = DecisionResource().export()
    dataset12 = VotingResultResource().export()
    dataset13 = DecisionDetailResource().export()
    dataset14 = InventoryResource().export()
    dataset15 = UsedInventoryResource().export()
    dataset16 = UsedInventoryDetailResource().export()
    dataset17 = LetterInResource().export()
    dataset18 = LetterOutResource().export()
    dataset19 = LetterOutExpeditionResource().export()
    dataset20 = AttachedExpeditionResource().export()
    dataset21 = CommunityLeadershipResource().export()
    dataset22 = ComplaintResource().export()
    dataset23 = MeetingTimeResource().export()
    dataset24 = VisitorResource().export()
    dataset25 = AttendanceResource().export()

    # Development
    dataset26 = NationalResource().export()
    dataset27 = ONGResource().export()
    dataset28 = AgencyResource().export()
    dataset29 = CompanyResource().export()
    dataset30 = ProjectResource().export()
    dataset31 = FundNationalResource().export()
    dataset32 = FundMunicipalityResource().export()
    dataset33 = FundONGResource().export()
    dataset34 = FundVolunteerResource().export()
    dataset35 = ImageProjectResource().export()
    dataset36 = ActivityResource().export()
    dataset37 = FundCommunityContributeResource().export()
    dataset38 = FundAgencyResource().export()
    dataset39 = ImageActivityResource().export()

    # Employee
    dataset40 = UserResource().export()
    dataset41 = EmployeeResource().export()
    dataset42 = EmployeeUserResource().export()

    with zipfile.ZipFile("media/dadusexport/"+naran_file, 'w') as csv_zip:
        # Population
        csv_zip.writestr("1-Livru_Rejistu_Populasaun.csv", dataset1.csv)
        csv_zip.writestr("2-Dadus_Custom_Ba_FamÍlia.csv", dataset3.csv)
        csv_zip.writestr("3-Dadus_Detail_FamÍlia.csv", dataset2.csv)
        csv_zip.writestr("4-Dadus_Migrasaun_Populasaun.csv", dataset5.csv)
        csv_zip.writestr("5-Dadus_Populasaun_Mudansa.csv", dataset6.csv)
        csv_zip.writestr("6-Dadus_Mudansa_Família.csv", dataset7.csv)
        csv_zip.writestr("7-Dadus_Populasaun_Temporáriu.csv", dataset4.csv)
        csv_zip.writestr("8-Dadus_Populsaun_Mate.csv", dataset8.csv)

        # Administration
        csv_zip.writestr("9-A7_Kargu.csv", dataset9.csv)
        csv_zip.writestr("10-A7_Periodu_Mandatu.csv", dataset10.csv)
        csv_zip.writestr("11-A1_&_A2_Livru_Desizaun_Suku.csv", dataset11.csv)
        csv_zip.writestr("12-A1_A2_Rezultadu_Votasaun_Desizaun_Suku.csv", dataset12.csv)
        csv_zip.writestr("13-A1_A2_Detaillu_Desizaun_Suku.csv", dataset13.csv)
        csv_zip.writestr("14-A3_Livru_Inventáriu_Suku.csv", dataset14.csv)
        csv_zip.writestr("15-A3_Inventáriu_Uzadu.csv", dataset15.csv)
        csv_zip.writestr("16-A3_Detallu_Inventáriu_Uzadu.csv", dataset16.csv)
        csv_zip.writestr("17-A5_Livru_Ajenda_Karta_Tama.csv", dataset17.csv)
        csv_zip.writestr("18-A4_Livru_Ajenda_Karta_Sai.csv", dataset18.csv)
        csv_zip.writestr("19-A6_Livru_Espedisaun.csv", dataset19.csv)
        csv_zip.writestr("20-A6_Aneksu_File_Espedisaun.csv", dataset20.csv)
        csv_zip.writestr("21-A7_Livru_Lideransa Komunitaria.csv", dataset21.csv)
        csv_zip.writestr("22-A10_Rejistu_Keixa_Suku.csv", dataset22.csv)
        csv_zip.writestr("23-A9_Minutas_Enkontru_Suku.csv", dataset23.csv)
        csv_zip.writestr("24-A11_Livru_Bainaka_Suku.csv", dataset24.csv)
        csv_zip.writestr("25-A8_Lista_Prezensa.csv", dataset24.csv)

        # Development
        csv_zip.writestr("26-Dadus_Custom_Ba_Nasional.csv", dataset26.csv)
        csv_zip.writestr("27-Dadus_Custom_Ba_ONG.csv", dataset27.csv)
        csv_zip.writestr("28-Dadus_Custom_Ba_Ajensia.csv", dataset28.csv)
        csv_zip.writestr("29-Dadus_Custom_Ba_Kompania.csv", dataset29.csv)
        csv_zip.writestr("30-C_1_Livru_Dadus_Projetu_Suku.csv", dataset30.csv)
        csv_zip.writestr("31-Fundus_Husi_Nasional.csv", dataset31.csv)
        csv_zip.writestr("32-Fundus_Husi_Munisípiu.csv", dataset32.csv)
        csv_zip.writestr("33-Fundus_Husi_ONG.csv", dataset33.csv)
        csv_zip.writestr("34-Fundus_Husi_Voluntáriu.csv", dataset34.csv)
        csv_zip.writestr("35-Aneksu_Imajen_Projetu.csv", dataset35.csv)
        csv_zip.writestr("36-C_2_Livru_Dadus_Atividade_Suku.csv", dataset36.csv)
        csv_zip.writestr("37-Fundus_Husi_Kontribuisaun_Komunidade.csv", dataset37.csv)
        csv_zip.writestr("38-Fundus_Husi_Ajénsia.csv", dataset38.csv)
        csv_zip.writestr("39-Aneksu_Imajen_Atividade.csv", dataset39.csv)

        # Employee
        csv_zip.writestr("40-Dadus_Users.csv", dataset40.csv)
        csv_zip.writestr("41-Dadus_Employee.csv", dataset41.csv)
        csv_zip.writestr("42-Dadus_EmployeeUser.csv", dataset42.csv) 

    print(naran_file)
    context = {
    "naranfile" : naran_file,'title':"Exporta"
    }
    return render(request, 'main/export/export.html',context)


