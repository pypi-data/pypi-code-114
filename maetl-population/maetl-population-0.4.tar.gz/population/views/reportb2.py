from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Level_Education,Temporary
from population.utils import getnewidp,getnewidf
from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,Death_form,Migration_form,Migrationout_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from django.db.models import Count
from django.contrib import messages
from django.db.models import Q
import datetime
from django.db.models.functions import ExtractYear
from django.utils.dateparse import parse_date


from django.shortcuts import get_object_or_404
from employee.models import *
from django.db.models import Q


@login_required
def reportb2(request):

    tinan1 = timezone.now().strftime("%Y")
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)


    feto  = Temporary.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(population__date_created__year=tinan1) &  Q(population__gender='f') & Q(population__type_data = 'te')).count()

    mane  = Temporary.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(population__date_created__year=tinan1) & Q(population__gender='m') & Q(population__type_data = 'te')).count()



    tinan = Population.objects.values(year=ExtractYear('date_register')).filter(Q(village =  userAddress.employee.village.id) & Q(type_data='te')).annotate(total=Count('id')).order_by('year')



    cidadaun = Citizen.objects.all()
    edukasaun = Level_Education.objects.all()


    context = {
        'title': 'Populasaun Suku',
        'tinan' : tinan,
        'title_tinan' : tinan1,
        'cidadaun' : cidadaun,
        'mane' : mane,
        'feto' : feto,
        'title' : 'Relatoriu dadus populasaun temporáriu',

        
    }
    return render(request, 'population/report/b2/report-b2.html',context)




@login_required
def reportb2_print(request):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    year = request.GET['tinan']
    tinan=""
    gender=""
    citizenp = ""
    dataagora = timezone.now()
    start_date = year + "-01-01"
    end_date = year + "-12-31"


    if request.GET['tinan'] != "jeral" :
        tinan = "Q(date_arive__range=(start_date, end_date))"

    if request.GET['gender'] != "jeral" :
        gender = " & Q(population__gender = request.GET['gender'])"

    if request.GET['citizenp'] != "jeral" :
        citizenp = " & Q(population__citizenp = request.GET['citizenp'])"


    editquerryset = "Temporary.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & "+ tinan + gender + citizenp + ")"


    dadostemporary = eval(editquerryset)


    context = {
        'title': 'Populasaun Suku',
        'dadostemporary' : dadostemporary,
        'tinan' : year,
        'title' : 'Relatorio Dados Populasaun Temporario',
		'munisipiu' : userAddress.employee.village.administrativepost.municipality.name,
		'postu' : userAddress.employee.village.administrativepost.name,
		'suku' : userAddress.employee.village.name,
    } 

    return render(request, 'population/report/b2/report-b2-print.html', context)