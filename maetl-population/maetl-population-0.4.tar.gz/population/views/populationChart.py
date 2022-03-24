from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Temporary,ChangeFamily
from population.utils import getnewidp,getnewidf
from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,CustumDetailFamily_form,Death_form,Migration_form,Migrationout_form,Changefamily_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import date
from django.http import JsonResponse
from employee.models import *
from datetime import datetime, timedelta


@login_required
def popchar_genderyear(request):
    currentYear = date.today().year
    labels = []
    data = []

    dataagora = timezone.now()
    start_date = "2000-01-01"
    end_date = dataagora + timedelta(1)

    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    if request.user.groups.all()[0].name == 'admin':
        querysets = DetailFamily.objects.filter(Q(population__date_register__range=(start_date, end_date)) & Q(status = True) & Q(population__id_family = 'i') & Q(population__status_datap = 'ac')).values('population__gender').annotate(count=Count('population__id'))
    else :
        querysets = DetailFamily.objects.filter(Q(population__date_register__range=(start_date, end_date)) & Q(status = True) & Q(population__id_family = 'i') & Q(population__status_datap = 'ac') & Q(population__village__id = userAddress.employee.village.id)).values('population__gender').annotate(count=Count('population__id'))


    for entry in querysets:
        sexu = ""
        if entry['population__gender'] == 'm' : 
            sexu = "Mane"
        if entry['population__gender'] == 'f' : 
            sexu = "Feto"
        if entry['population__gender'] == 's' : 
            sexu = "Seluk"

        labels.append(sexu)
        data.append(entry['count'])
    return JsonResponse(data={
		'labels':labels,
		'data':data,
		})


@login_required
def popchar_temporary(request):
    currentYear = date.today().year
    labels = []
    data = []

    dataagora = timezone.now()
    start_date = str(currentYear) + "-01-01"
    end_date = dataagora

    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    if request.user.groups.all()[0].name == 'admin':
        querysets = Temporary.objects.filter(Q(date_arive__range=(start_date, end_date))  & (Q(population__type_data = 'te') | Q(population__type_data = 'mo'))).values('population__gender').annotate(count=Count('id'))
    else : 
        querysets = Temporary.objects.filter(Q(date_arive__range=(start_date, end_date)) & Q(population__village__id = userAddress.employee.village.id)  & (Q(population__type_data = 'te') | Q(population__type_data = 'mo'))).values('population__gender').annotate(count=Count('id'))


    for entry in querysets:

        print(entry['count'])
        sexu = ""
        if entry['population__gender'] == 'm' : 
            sexu = "Mane"
        elif entry['population__gender'] == 'f' : 
            sexu = "Feto"
        elif entry['population__gender'] == 's' : 
            sexu = "Seluk"

        labels.append(sexu)
        data.append(entry['count'])
    return JsonResponse(data={
		'labels':labels,
		'data':data,
		})
        


def popchar_changes(request):
    currentYear = date.today().year
    labels = []
    data = []

    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    tinan = timezone.now().strftime("%Y")

    
    if request.user.groups.all()[0].name == 'admin':

        moris  = Population.objects.filter(Q(date_of_bird__year = tinan) & Q(village__id = userAddress.employee.village.id)  & Q(id_family = 'i') & Q(type_data = 'f')).count()


        labels.append("Moris")
        data.append(moris)

        mate  = Death.objects.filter(Q(date__year = tinan) & Q(population__status_datap = 'ma')).count()
        labels.append("Mate")
        data.append(mate)

        muda_sai  = Migrationout.objects.filter(Q(date_migration__year = tinan)  & Q(population__status_datap = 'mu')).count()
        labels.append("Muda Sai")
        data.append(muda_sai)


        muda_tama  = DetailFamily.objects.filter(Q(population__date_register__year = tinan)  & Q(population__type_data = 'm')).count()
        labels.append("Muda Tama")
        data.append(muda_tama)

    else :

        moris  = Population.objects.filter(Q(date_of_bird__year = tinan) & Q(village__id = userAddress.employee.village.id)  & Q(id_family = 'i') & Q(type_data = 'f')).count()


        labels.append("Moris")
        data.append(moris)

        mate  = Death.objects.filter(Q(date__year = tinan) & Q(population__village__id = userAddress.employee.village.id) & Q(population__status_datap = 'ma')).count()
        labels.append("Mate")
        data.append(mate)

        muda_sai  = Migrationout.objects.filter(Q(date_migration__year = tinan) & Q(population__village__id = userAddress.employee.village.id) & Q(population__status_datap = 'mu')).count()
        labels.append("Muda Sai")
        data.append(muda_sai)


        muda_tama  = DetailFamily.objects.filter(Q(population__date_register__year = tinan) & Q(population__village__id = userAddress.employee.village.id) & Q(population__type_data = 'm')).count()
        labels.append("Muda Tama")
        data.append(muda_tama)
        

    

    return JsonResponse(data={
		'labels':labels,
		'data':data,
		})


