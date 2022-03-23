from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from custom.models import Municipality,AdministrativePost,Village,Aldeia
from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,User,Migration,Death,Migrationout,Level_Education
from population.utils import getnewidp,getnewidf
from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,Death_form,Migration_form,Migrationout_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from django.db.models import Count
from django.contrib import messages

import datetime
from django.db.models.functions import ExtractYear
from django.utils.dateparse import parse_date
from datetime import date
from django.shortcuts import get_object_or_404
from employee.models import *
from django.db.models import Q


@login_required
def reportb1jeralMunicipality(request):
    currentYear = date.today().year
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    municipality = Population.objects.filter(Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).values('municipality__name','municipality__id').annotate(count=Count('municipality__id')).order_by('municipality__id')

    totalpop = Population.objects.filter(Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).values('municipality__name','municipality__id').count()


    context = {
        'title': 'Populasaun Suku',
        'tinan' : currentYear,
        'title_tinan' : currentYear,
        'municipality' : municipality,
        'totalpop' : totalpop,
        'title' : 'Relatorio Dados Populasaun Iha Kada Munisipiu',  
    }
    return render(request, 'population/reportjeral/b1/reportjeral-b1.html',context)


@login_required
def reportb1jeralPostadministrative(request,id):
    currentYear = date.today().year

    munisipiu = Municipality.objects.get(id=id)
    postu = Population.objects.filter(Q(municipality= id) & Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).values('administrativepost__name','administrativepost__id').annotate(count=Count('id')).order_by('administrativepost__id')

    totalpop = Population.objects.filter(Q(municipality= id) & Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).count()

    context = {
        'title': 'Populasaun Suku',
        'postu' : postu,
        'id' : id,
        'totalpop' : totalpop,
        'munisipiu' : munisipiu.name,
        'title' : 'Relatorio Dados Populasaun Kada Postu Administrativu' +  munisipiu.name  ,  
    }
    return render(request, 'population/reportjeral/b1/reportjeral-b1-administrative.html',context)



@login_required
def reportb1jeralVillage(request,id):
    currentYear = date.today().year
    postu = AdministrativePost.objects.get(id=id)
    suku = Population.objects.filter(Q(administrativepost= id)  & Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).values('village__name','village__id').annotate(count=Count('village__id')).order_by('village__id')

    totalpop = Population.objects.filter(Q(administrativepost= id)  & Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).count()

    context = {
        'title': 'Populasaun Suku',
        'suku' : suku,
        'id' : id,
        'totalpop' : totalpop,
        'postu' : postu.name,
        'id_munisipiu' : postu.municipality.id,
        'munisipiu' : postu.municipality.name,
        'title' : 'Relatorio Dados Populasaun iha kada suku ',  
    }
    return render(request, 'population/reportjeral/b1/reportjeral-b1-village.html',context)



@login_required
def reportb1jeralAldeia(request,id):
    currentYear = date.today().year
    
    suku = Village.objects.get(id=id)

    aldeia = Population.objects.filter(Q(village = id)  & Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).values('aldeia__name','aldeia__id').annotate(count=Count('aldeia__id')).order_by('aldeia__id')
    
    totalpop = Population.objects.filter(Q(village = id)  & Q(date_register__year=currentYear)  & Q(id_family = 'i') & Q(status_datap = 'ac')).count()

    context = {
        'title': 'Populasaun Suku',
        'aldeia' : aldeia,
        'id' : id,
        'suku' : suku.name,
        'totalpop' : totalpop,
        'id_postu' : suku.administrativepost.id,
        'postu' : suku.administrativepost.name,
        'munisipiu' : suku.administrativepost.municipality.name,
        'title' : 'Relatorio Dados Populasaun iha kada aldeia',  
    }
    return render(request, 'population/reportjeral/b1/reportjeral-b1-aldeia.html',context)






@login_required
def reportb1_printjeral(request):     
    family_member = []
    familymember_list = DetailFamily.objects.filter(Q(population__status_datap = 'ac') & Q(status = True)).order_by("population__municipality")
    count = 0
    for dados in familymember_list.iterator():
            count = count + 1
        
            family_member.append({
                'family' : dados.family.id_family,
                'family_position' : dados.family_position,
                'id': dados.population.id,
                'hashed' : dados.hashed,
                'village': dados.population.village, 
                'aldeia':  str(dados.population.aldeia) +" / "+ str(dados.population.aldeia.village) +" / "+  str(dados.population.aldeia.village.administrativepost) +" / "+  str(dados.population.aldeia.village.administrativepost.municipality) , 
                'profession': dados.population.profession,
                'citizenp': dados.population.citizenp,
                'religion': dados.population.religion, 
                'user_created': dados.population.user_created,
                'name': dados.population.name,
                'date_of_bird': dados.population.date_of_bird, 
                'place_of_bird': dados.population.place_of_bird,
                'gender': dados.population.gender,
                'marital_status': dados.population.marital_status,
                'level_education': dados.population.level_education, 
                'readalatin': dados.population.readalatin, 
                'readaarabe': dados.population.readaarabe,
                'readachina': dados.population.readachina,
                'nu_bi': dados.population.nu_bi,
                'id_family': dados.family,
                'descriptionp': dados.population.descriptionp,
                'imagen': dados.population.imagen, 
                'status_datap': dados.population.status_datap,
                'type_data': dados.population.type_data,
                'date_created': dados.population.date_created,
                })
    context = {
        'title': 'Populasaun Suku',
        'family_member' : family_member,
        'title' : 'Relatorio Dados Populasaun suku',
        
    }
    return render(request, 'population/reportjeral/b1/reportjeral-b1-print.html', context)




@login_required
def reportb1_printPostadministrative(request,id):     
    family_member = []
    familymember_list = DetailFamily.objects.filter(Q(population__status_datap = 'ac') & Q(status = True) & Q(population__municipality__id = id) ).order_by("population__municipality")
    count = 0
    for dados in familymember_list.iterator():
            count = count + 1
        
            family_member.append({
                'family' : dados.family.id_family,
                'family_position' : dados.family_position,
                'id': dados.population.id,
                'hashed' : dados.hashed,
                'village': dados.population.village, 
                'aldeia':  str(dados.population.aldeia) +" / "+ str(dados.population.aldeia.village) +" / "+  str(dados.population.aldeia.village.administrativepost) +" / "+  str(dados.population.aldeia.village.administrativepost.municipality) , 
                'profession': dados.population.profession,
                'citizenp': dados.population.citizenp,
                'religion': dados.population.religion, 
                'user_created': dados.population.user_created,
                'name': dados.population.name,
                'date_of_bird': dados.population.date_of_bird, 
                'place_of_bird': dados.population.place_of_bird,
                'gender': dados.population.gender,
                'marital_status': dados.population.marital_status,
                'level_education': dados.population.level_education, 
                'readalatin': dados.population.readalatin, 
                'readaarabe': dados.population.readaarabe,
                'readachina': dados.population.readachina,
                'nu_bi': dados.population.nu_bi,
                'id_family': dados.family,
                'descriptionp': dados.population.descriptionp,
                'imagen': dados.population.imagen, 
                'status_datap': dados.population.status_datap,
                'type_data': dados.population.type_data,
                'date_created': dados.population.date_created,
                })
    context = {
        'title': 'Populasaun Suku',
        'family_member' : family_member,
        'title' : 'Relatorio Dados Populasaun suku',
        
    }
    return render(request, 'population/reportjeral/b1/reportjeral-b1-print.html', context)



@login_required
def reportb1_printVillage(request,id):     
    family_member = []
    familymember_list = DetailFamily.objects.filter(Q(population__status_datap = 'ac') & Q(status = True) & Q(population__administrativepost__id = id) ).order_by("population__administrativepost")
    count = 0
    for dados in familymember_list.iterator():
            count = count + 1
        
            family_member.append({
                'family' : dados.family.id_family,
                'family_position' : dados.family_position,
                'id': dados.population.id,
                'hashed' : dados.hashed,
                'village': dados.population.village, 
                'aldeia':  str(dados.population.aldeia) +" / "+ str(dados.population.aldeia.village) +" / "+  str(dados.population.aldeia.village.administrativepost) +" / "+  str(dados.population.aldeia.village.administrativepost.municipality) , 
                'profession': dados.population.profession,
                'citizenp': dados.population.citizenp,
                'religion': dados.population.religion, 
                'user_created': dados.population.user_created,
                'name': dados.population.name,
                'date_of_bird': dados.population.date_of_bird, 
                'place_of_bird': dados.population.place_of_bird,
                'gender': dados.population.gender,
                'marital_status': dados.population.marital_status,
                'level_education': dados.population.level_education, 
                'readalatin': dados.population.readalatin, 
                'readaarabe': dados.population.readaarabe,
                'readachina': dados.population.readachina,
                'nu_bi': dados.population.nu_bi,
                'id_family': dados.family,
                'descriptionp': dados.population.descriptionp,
                'imagen': dados.population.imagen, 
                'status_datap': dados.population.status_datap,
                'type_data': dados.population.type_data,
                'date_created': dados.population.date_created,
                })
    context = {
        'title': 'Populasaun Suku',
        'family_member' : family_member,
        'title' : 'Relatorio Dados Populasaun suku',
        
    }
    return render(request, 'population/reportjeral/b1/reportjeral-b1-print.html', context)