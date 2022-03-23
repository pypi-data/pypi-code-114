from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Level_Education,Temporary,DetailFamily
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

from django.shortcuts import get_object_or_404
from employee.models import *
from django.db.models import Q

@login_required
def reportb3(request):

    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    tinan = timezone.now().strftime("%Y")
    title_year = tinan

       # editquerryset = "Migrationout.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(date_migration__year = request.GET['tinan']) & Q(population__status_datap = 'mu')" + gender + tinan + ")"
      
    tinan_list = []
    dados_tinan = []
    tinan = Population.objects.values(year=ExtractYear('date_register')).filter(Q(village_id = userAddress.employee.village.id)).annotate(total=Count('id')).order_by('year')
    muda_tamatt = Migration.objects.values(year=ExtractYear('date_migration')).filter(Q(village_id = userAddress.employee.village.id) & Q(population__id_family = 'i')).annotate(total=Count('id')).order_by('year')
    moristt = DetailFamily.objects.values(year=ExtractYear('population__date_of_bird')).filter(Q(population__village__id = userAddress.employee.village.id) & Q(population__id_family = 'i') & Q(status = True) & Q(population__type_data = 'f')).annotate(total=Count('id')).order_by('year')
    matett = Death.objects.values(year=ExtractYear('date')).filter(Q(population__village__id = userAddress.employee.village.id) &  Q(population__status_datap = 'ma')).annotate(total=Count('id')).order_by('year')
    musasaitt = Migrationout.objects.values(year=ExtractYear('date_migration')).filter(Q(population__village__id = userAddress.employee.village.id) & Q(population__status_datap = 'mu')).annotate(total=Count('id')).order_by('year')

    for tinan in muda_tamatt :
        tinan_list.append({
            "tinan" : tinan['year'],
            })
    for tinan in moristt :
        tinan_list.append({
            "tinan" : tinan['year'],
            })
    for tinan in matett :
        tinan_list.append({
            "tinan" : tinan['year'],
            })
    for tinan in musasaitt :
        tinan_list.append({
            "tinan" : tinan['year'],
            })
    for datat in tinan_list :

        if datat['tinan']  in dados_tinan :
             print("")
        else : 
            dados_tinan.append(datat['tinan'])
            
    dados_tinan.sort()














    cidadaun = Citizen.objects.all()
    edukasaun = Level_Education.objects.all()
    context = {
        'title': 'Populasaun Suku',
        'tinan' : tinan,
        'cidadaun' : cidadaun,
        'title_year' : title_year,
        'dados_tinan' : dados_tinan,
     
        'title' : 'Relatoriu dadus mudansa populasaun',
        
    }
    return render(request, 'population/report/b3/report-b3.html',context)




@login_required
def reportb3_print(request):


    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)


    year = request.GET['tinan']
    tinan=""
    gender=""
    citizenp = ""
    dadosmudansa = ""
    title = ""
    tipu = ""
    dadosmudansa1 = ""
    dadosmudansa2 = ""
    dadosmudansa3 = ""
    dadosmudansa4 = ""

    dadosmudansapop = []
        
    template = "population/report/b3/report-b3print.html" 


    # if request.GET['tinan'] != "jeral" :
    #     tinan = "Q(date_created__year = request.GET['tinan'])"

    if request.GET['gender'] != "jeral" :
        gender = " & Q(population__gender = request.GET['gender'])"
    

    
    if request.GET['mudansa'] == "muda_tama" or request.GET['mudansa'] == 'jeral' :
        template = "population/report/b3/report-b3muda_tama.html"
        editquerryset = "Migration.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(population__id_family = 'i') & Q(date_migration__year = request.GET['tinan']) " + gender + tinan + ")"

        tipu = "muda_tama"

       
        dadosmudansa1 = eval(editquerryset)

        #prosesu foti dados nasionalidade husi populasaun
        for dados in dadosmudansa1 :
            husi = ""

            if dados.cidadaunm.id == 1 :
                husi = dados.from_aldeia

            elif dados.cidadaunm.id == 2 :
                husi = dados.from_nation
   
                # except Death.DoesNotExist:
            #hatama dados populasaun mate ba iha forma aray tuir formatu livru mudansa populasaun  hodi haruka ba iha template  
            dadosmudansapop.append({
                'name' : dados.population.name,
                'place_of_bird' : dados.population.place_of_bird,
                'date_of_bird' : dados.population.date_of_bird,
                'gender' : dados.population.gender,
                'citizen' : dados.population.nationality,
                'asaun' : husi ,
                'data' : dados.date_migration,
                'obs' : dados.descriptionm,
                'tipu' : tipu,
            })




    if  request.GET['mudansa'] == "moris" or  request.GET['mudansa'] == 'jeral'  :

        template = "population/report/b3/report-b3moris.html"
        editquerryset = "DetailFamily.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(population__date_of_bird__year = request.GET['tinan']) & Q(population__id_family = 'i') & Q(status = True) & Q(population__type_data = 'f')" + gender + tinan + ")"
        tipu = "moris"


        dadosmudansa2 = eval(editquerryset)
        #prosesu foti dados nasionalidade husi populasaun
        for dados in dadosmudansa2 :
 
                # except Death.DoesNotExist:
            #hatama dados populasaun mate ba iha forma aray tuir formatu livru mudansa populasaun  hodi haruka ba iha template  
            dadosmudansapop.append({
                'name' : dados.population.name,
                'place_of_bird' : dados.population.place_of_bird,
                'date_of_bird' : dados.population.date_of_bird,
                'gender' : dados.population.gender,
                'citizen' : dados.population.nationality,
                'asaun' : 'mamuk' ,
                'data' : dados.population.date_of_bird,
                'obs' : dados.population.descriptionp,
                'tipu' : tipu,
            })

    


    # prosesu bolu dados populasaun ne'ebe mate tuir tinan
    if  request.GET['mudansa'] == "mate" or  request.GET['mudansa'] == 'jeral' :
        template = "population/report/b3/report-b3mate.html"
        editquerryset = "Death.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(date__year = request.GET['tinan']) & Q(population__status_datap = 'ma') " + gender + tinan + ")"
        tipu = "mate"

        dadosmudansa3 = eval(editquerryset)
        #prosesu foti dados nasionalidade husi populasaun
        for dados in dadosmudansa3 :
 
                # except Death.DoesNotExist:
            #hatama dados populasaun mate ba iha forma aray tuir formatu livru mudansa populasaun  hodi haruka ba iha template  
            dadosmudansapop.append({
                'name' : dados.population.name,
                'place_of_bird' : dados.population.place_of_bird,
                'date_of_bird' : dados.population.date_of_bird,
                'gender' : dados.population.gender,
                'citizen' : dados.population.nationality,
                'asaun' : 'mamuk' ,
                'data' : dados.date,
                'obs' : dados.descriptiond,
                'tipu' : tipu,
            })
    

    if  request.GET['mudansa'] == "muda_sai" or  request.GET['mudansa'] == 'jeral' :
        template = "population/report/b3/report-b3muda_sai.html"
        #dados populasaun muda sai  foti husi dados populasaun migrasaun
        editquerryset = "Migrationout.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(date_migration__year = request.GET['tinan']) & Q(population__status_datap = 'mu')" + gender + tinan + ")"
        dadosmudansa4 = eval(editquerryset)
        tipu = "muda_sai"
        for dados in dadosmudansa4 :

            dadosmudansapop.append({
                'name' : dados.population.name,
                'place_of_bird' : dados.population.place_of_bird,
                'date_of_bird' : dados.population.date_of_bird,
                'gender' : dados.population.gender,
                'citizen' : dados.population.nationality,
                'asaun' : "mamuk" ,
                'data' : dados.date_migration,
                'obs' : dados.descriptionmo,
                'tipu' : tipu,
            })
        
        tipu = "muda_sai"


    koko = request.GET['mudansa']
    if  koko == 'jeral' :

        template = "population/report/b3/report-b3print.html" 

 
 
    

    context = {
        'title' : 'Relatorio Dados Mudansa Populasaun',
        'dadosmudansapop' : dadosmudansapop,
        'dadosmudansa' : dadosmudansa,
        'dadosmudansa1' : dadosmudansa1,
        'dadosmudansa2' : dadosmudansa2,
        'dadosmudansa3' : dadosmudansa3,
        'dadosmudansa4' : dadosmudansa4,
        'year' : year,
        'tinan' : tinan,
        'tipu'  : tipu,
		'munisipiu' : userAddress.employee.village.administrativepost.municipality.name,
		'postu' : userAddress.employee.village.administrativepost.name,
		'suku' : userAddress.employee.village.name,

    } 

    return render(request,template, context)