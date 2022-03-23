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



@login_required
def popchar_munisipality(request):
    currentYear = date.today().year
    labels = []
    data = []
    
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    querysets = Population.objects.filter(Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).values('municipality__name').annotate(count=Count('municipality__id'))
    for entry in querysets:
        labels.append(entry['municipality__name'])
        data.append(entry['count'])
    return JsonResponse(data={
		'labels':labels,
		'data':data,
		})


def popchar_postadministrative(request,id):
    currentYear = date.today().year
    labels = [] 
    data = []
    postu = Population.objects.filter(Q(municipality= id)  & Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).values('administrativepost__name','administrativepost__id').annotate(count=Count('id')).order_by('administrativepost__id')

    for entry in postu:
        labels.append(entry['administrativepost__name'])
        data.append(entry['count'])
    return JsonResponse(data={
		'labels':labels,
		'data':data,
		})


def popchar_village(request,id):
    currentYear = date.today().year
    labels = [] 
    data = []
    postu = Population.objects.filter(Q(administrativepost= id)  & Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).values('village__name','village__id').annotate(count=Count('village__id')).order_by('village__id')

    for entry in postu:
        labels.append(entry['village__name'])
        data.append(entry['count'])
    return JsonResponse(data={
		'labels':labels,
		'data':data,
		})

def popchar_aldeia(request,id):
    currentYear = date.today().year
    labels = [] 
    data = []
    postu = Population.objects.filter(Q(village = id)  & Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).values('aldeia__name','aldeia__id').annotate(count=Count('aldeia__id')).order_by('aldeia__id')

    for entry in postu:
        labels.append(entry['aldeia__name'])
        data.append(entry['count'])
    return JsonResponse(data={
		'labels':labels,
		'data':data,
		})