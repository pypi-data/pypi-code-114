from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from population.models import Population,DetailFamily,Deficient,Language,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Level_Education
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
def reportb1(request):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    tinan1 = timezone.now().strftime("%Y")

    mane  = DetailFamily.objects.filter(Q(population__village__id = userAddress.employee.village.id) & Q(date_created__year = tinan1) & Q(population__status_datap='ac') & Q(status = True) & Q(population__gender='m')).count()

    feto  = DetailFamily.objects.filter(Q(population__village__id = userAddress.employee.village.id) & Q(date_created__year = tinan1) & Q(status = True)  & Q(population__status_datap='ac') & Q(population__gender='f')).count()

   
    tinan = Population.objects.values(year=ExtractYear('date_register')).filter(Q(village__id = userAddress.employee.village.id) & Q(type_data='p') | Q(type_data='f') | Q(type_data='m')).annotate(total=Count('id')).order_by('year')

    relijiaun = Religion.objects.all()
    edukasaun = Level_Education.objects.all()
    kondisaun = Deficient.objects.all()
    profession = Profession.objects.all()
    aldeia = Aldeia.objects.filter(Q(village__id = userAddress.employee.village.id))
    



    context = {
        'title': 'Populasaun Suku',
        'tinan' : tinan,
        'title_tinan' : tinan1,
        'relijiaun' : relijiaun,
        'edukasaun' : edukasaun,
        'kondisaun' : kondisaun,
        'profession' : profession,
        'aldeia' : aldeia,
        'mane' : mane,
        'feto' : feto,
        'title' : 'Relatorio Dados Populasaun suku',
        
        
    }
    return render(request, 'population/report/b1/report-b1.html',context)




@login_required
def reportb1_print(request):

    year = request.GET['tinan']
    tinan=""
    gender=""
    citizenp = ""
    religion = ""
    level_education = ""
    kondisaun = ""
    vurneravel = ""
    vurdata = ""
    marital_status = ""
    profession = ""
    aldeia = ""

    titulu_kategoria = ""

    dataexport = request.GET['dados']
  
    tinan_title = "Dados "

    if  dataexport == 'excel' :
        template ="population/report/b1/report-b1-excel.html"
    else :
        template ="population/report/b1/report-b1-print.html"



    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    if request.GET['aldeia'] != "jeral" :
        aldeia = " & Q(family__aldeia = request.GET['aldeia'])"
        naran_ald = Aldeia.objects.get(id=request.GET['aldeia'])
        titulu_kategoria = titulu_kategoria + " ( Aldeia : " + naran_ald.name + ")"


    if request.GET['tinan'] != "jeral" :
        tinan = " & Q(population__date_register__year = request.GET['tinan'])"
        tinan_title = tinan_title + "Populasaun Tinan" + tinan
        titulu_kategoria = titulu_kategoria + " ( Tinan : "  + request.GET['tinan'] + ") "

    if request.GET['kondisaun'] != "jeral" :
        kondisaun = "& Q(population__deficient = request.GET['kondisaun'])"
        naran_kond = Deficient.objects.get(id=request.GET['kondisaun'])
        titulu_kategoria = titulu_kategoria + " (Kondisaun Fiziku :"+ naran_kond.name +" )" 


    if request.GET['vurneravel'] != "jeral" :
        if request.GET['vurneravel'] == 'True' :
            vurneravel = "& Q(population__vulnerable = True )"

        elif request.GET['vurneravel'] == 'False' :
            vurneravel = "& Q(population__vulnerable = False )"
            titulu_kategoria = titulu_kategoria + " ( Populasaun : Vurneralvel)"




    if request.GET['gender'] != "jeral" :
        gender = " & Q(population__gender = request.GET['gender'])"
        titulu_kategoria = titulu_kategoria + " ( Sexu : " + request.GET['gender'] + ")"


  

    if request.GET['citizenp'] != "jeral" :
        citizenp = " & Q(population__citizenp = request.GET['citizenp'])"
        if request.GET['citizenp'] == 'a' :
            titulu_kategoria = titulu_kategoria + " (Sidadaun : Adkeridu)"
        elif request.GET['citizenp'] == 'o' :
            titulu_kategoria = titulu_kategoria + " (Sidadaun : Orijinal)"


    
    if request.GET['religion'] != "jeral" :
        religion = " & Q(population__religion = request.GET['religion'])"
        naran_relig = Religion.objects.get(id=request.GET['religion'])
        titulu_kategoria = titulu_kategoria + " (Relijiaun :"+ naran_relig.name +" )" 


    if request.GET['profession'] != "jeral" :
        profession = " & Q(population__profession = request.GET['profession'])"
        naran_prof = Profession.objects.get(id=request.GET['profession'])
        titulu_kategoria = titulu_kategoria + " (Profisaun :"+ naran_prof.name +" )" 



    if request.GET['marital_status'] != "jeral" :

        marital_code = request.GET['marital_status']
        marital_status = " & Q(population__marital_status = request.GET['marital_status'])"

        if marital_code == "s" :
            titulu_kategoria = titulu_kategoria + " (Estadu Civil : Klosan )" 
        elif marital_code == "c" :
            titulu_kategoria = titulu_kategoria + " (Estadu Civil : Kaben Nain )" 
        elif marital_code == "d" :
            titulu_kategoria = titulu_kategoria + " (Estadu Civil : Fahe Malu )" 
        elif marital_code == "f" :
            titulu_kategoria = titulu_kategoria + " (Estadu Civil : Faluk )" 


    if request.GET['level_education'] != "jeral" :
        level_education = " & Q(population__level_education = request.GET['level_education'])"
        naran_edu = Level_Education.objects.get(id=request.GET['level_education'])
        titulu_kategoria = titulu_kategoria + " (Habilitasaun Literariu :"+ naran_edu.name +" )" 
    
    # if request.GET['lingua'] != "jeral" :

    #     if request.GET["lingua"] == 'a' :
    #         lingua = " & Q(population__readaarabe = 's')"
        
    #     if request.GET['lingua'] != "l" :
    #         lingua = " & Q(population__readalatin = 's')"

    #     if request.GET['lingua'] != "c" :
    #         lingua = " & Q(population__readachina = 's')"
            
        


    editquerryset = "DetailFamily.objects.filter(Q(population__village__id = userAddress.employee.village.id) "+ tinan + kondisaun  + citizenp + religion + level_education  +  vurneravel  + gender  + marital_status + profession + aldeia +  " & Q(population__status_datap = 'ac') & Q(status = True)).values('family').annotate(total=Count('family')).order_by('family')"

    dadosfamily = eval(editquerryset)




    family_member = []
    numb = 0 

    for dados1 in dadosfamily:
        numb = numb + 1
        typenum = 'parimpar'
        cektype  = numb % 2
        
        if cektype == 0 :
            typenum = 'par'
        else : 
            typenum = 'impar'
        familia = " & Q(family = dados1['family']) & Q(population__status_datap = 'ac') & Q(status = True)"

        editquerryset2 = "DetailFamily.objects.filter(Q(population__village__id = userAddress.employee.village.id) "+ tinan + kondisaun  + citizenp + religion + level_education  + familia + vurneravel  + gender + marital_status + profession + aldeia + ")"


 

        familymember_list = eval(editquerryset2)   

        count = 0
        for dados in familymember_list.iterator():
            count = count + 1


            linguadata = ""
            datalingua = ""
            linguamaterna = ""


            if dados.population.language != None :
                datalingua = dados.population.language
                datalingua = datalingua.split('*#')
                linguamaterna = datalingua[1]
                datalingua = datalingua[0]
                datalingua = datalingua.split('-')
            else : 
                linguadata = "Dadus Laiha"



            
            if linguamaterna == "" :
                linguamaterna = "Dadus Laiha"

          
            lingualop = []
            language = Language.objects.all()
            
            for dadoslingua in language : 
                if str(dadoslingua.id) in datalingua :
                    linguadata = linguadata + "- " + dadoslingua.name + "  "

            if linguadata  == "" :
                linguadata =" Dadus Laiha"




        
            family_member.append({
                'numb' : numb,
                'typenum' : typenum,
                'count' : count,
                'total' : dados1['total'],
                'family' : dados.family.id_family,
                'family_position' : dados.family_position,
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
                'nu_p': dados.population.nu_p,
                'nu_e': dados.population.nu_e,
                'phone': dados.population.phone,
                'id_family': dados.family,
                'kondisaun' : dados.population.deficient,
                'descriptionp': dados.population.descriptionp,
                'imagen': dados.population.imagen, 
                'status_datap': dados.population.status_datap,
                'type_data': dados.population.type_data,
                'date_created': dados.population.date_created,
                'data_rejistu' : dados.population.date_register,
                'lingua': "Lingua Internasional :  " + linguadata + " , Lingua Materna : " + linguamaterna,
                'nu_e': dados.population.nu_e,
                'nu_p': dados.population.nu_p,
                'kondisaun': dados.population.deficient,
                'phone': dados.population.phone,
                'vulnerable': dados.population.vulnerable,
                })
    context = {
        'title': 'Populasaun Suku',
        'family_member' : family_member,
        'totpop' : len(family_member),
        
        'tinan' : year,
        'title' : 'Relatorio Dados Populasaun suku',
        'titulu_kategoria' : titulu_kategoria,
		'munisipiu' : userAddress.employee.village.administrativepost.municipality.name,
		'postu' : userAddress.employee.village.administrativepost.name,
		'suku' : userAddress.employee.village.name,

        
    }
    return render(request, template, context)