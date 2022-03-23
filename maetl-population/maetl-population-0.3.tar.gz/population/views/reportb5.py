from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Level_Education,Temporary,ChangeFamily
from population.utils import getnewidp,getnewidf
from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,Death_form,Migration_form,Migrationout_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from population.utils import getfulan
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
def reportb5(request):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)


    totalmembru =  DetailFamily.objects.values('family').filter(Q(population__village__id =  userAddress.employee.village.id)).annotate(total=Count('family')).order_by('family')
    
    family_list = Family.objects.filter(village = userAddress.employee.village.id).order_by("id_family")

    lista_familia = []
    membru = "Dadus Laiha (0)"

    for dados in family_list.iterator():
        totalmembru =  DetailFamily.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(family__id_family = dados.id_family) & Q(status = True)).count()

        pessoa =  DetailFamily.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(family__id_family = dados.id_family) & Q(status = True))
        membru = ""
        tot_chefe = 0


        for data in pessoa.iterator():
            membru = membru + data.family_position.name + data.population.name + " , "
            if data.family_position.id == 1 :
                tot_chefe = 1

        if membru == "" :
            membru = "Dados Laiha (0)"
            
        lista_familia.append({
            'id_family' : dados.id_family,
            'aldeia' : dados.aldeia,
            'data_registu' : dados.data_registu,
            'total' : totalmembru,
            'hashed' : dados.hashed,
            'tot_chefe' : tot_chefe,
            'membru' : membru  
        })

    family_list = Family.objects.filter(village = "1")
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Populasaun Suku',
        'family_list' : family_list,
        'lista_familia' : lista_familia,
        'total_family' : len(family_list),

    }

    return render(request, 'population/report/b5/report-b5.html',context)




@login_required
def reportb5_print(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)


    familia = Family.objects.get(hashed = hashed)
    familymember_list = DetailFamily.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(family = familia)).order_by('family_position')


    family_member = []
    chefe_fam = ""
    aldeia = ""
    id_fam = ""
    imagen = ""

    
    

    for dados in familymember_list.iterator():

        try:
            mate = Death.objects.get(population = dados.population.id)
            dekrisaunmate = mate.descriptiond
            datamate = mate.date
        except Death.DoesNotExist:
            dekrisaunmate = 'laiha'
            datamate = 'laiha'

        try:
            sai = Migrationout.objects.get(population = dados.population.id)
            dekrisaunsai = sai.descriptionmo
            datasai = sai.date_migration
        except Migrationout.DoesNotExist:
            dekrisaunsai = 'laiha'
            datasai = 'laiha'

        try:
            troka = ChangeFamily.objects.get(familymember = dados.id)
            dekrisauncf = troka.descriptioncf
            datacf = troka.date_change
        except ChangeFamily.DoesNotExist:
            dekrisauncf = 'laiha'
            datacf = 'laiha'



        if dados.family_position.id == 1:
            chefe_fam = dados.population.name
            id_fam = dados.family.id_family
            imagen = dados.population.imagen
            aldeia = dados.family.aldeia.name


      
        family_member.append({
            'dekrisauncf' : dekrisauncf,
            'status_datap' : dados.population.status_datap,
            'datacf' : datacf,
            'family_position' : dados.family_position,
            'dekrisaunmate' : dekrisaunmate,
            'datamate' : datamate,
            'dekrisaunsai' : dekrisaunsai,
            'datasai' : datasai,
            'id': dados.population.id,
            'hashed' : dados.hashed,
            'village': dados.population.village, 
            'aldeia': dados.population.aldeia, 
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
            'id_family': dados.population.id_family,
            'descriptionp': dados.population.descriptionp,
            'imagen': dados.population.imagen, 
            'status_datap': dados.population.status_datap,
            'type_data': dados.population.type_data,
            'date_created': dados.population.date_created,
            'nu_e': dados.population.nu_e,
            'nu_p': dados.population.nu_p,
            'kondisaun': dados.population.deficient,
            'phone': dados.population.phone,
            'vulnerable': dados.population.vulnerable,
            })

 

    context = {
        'title': 'Detallu familia',
        'familymember_list' : familymember_list,
        'hashed' : hashed,
        'dataagora' : timezone.now(),
        'family_member' : family_member,
        'id_familia' : familia.id_family,
        'chefe_fam' : chefe_fam,
        'id_fam' : f"{id_fam:010}",
        'imagen' : imagen,
		'munisipiu' : userAddress.employee.village.administrativepost.municipality.name,
		'postu' : userAddress.employee.village.administrativepost.name,
		'suku' : userAddress.employee.village.name,
        'aldeia' : aldeia,
        'title' : 'Relatorio Dados Uma kain(Fixa Familia)',
    }
    return render(request, 'population/report/b5/report-b5-print.html', context)