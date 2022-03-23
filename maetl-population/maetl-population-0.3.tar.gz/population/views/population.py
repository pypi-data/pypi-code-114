from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from population.models import Population,Language,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Temporary,ChangeFamily
from population.utils import getnewidp,getnewidf
from population.forms import Family_form,Population2_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,CustumDetailFamily_form,Death_form,Migration_form,Migrationout_form,Changefamily_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from custom.utils import getnewid, getjustnewid, hash_md5, getlastid

from population.utils import getlastid_kinos,getlastid_kinosrp


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


@login_required
def dashboard_population(request):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    tinan = timezone.now().strftime("%Y")

    # totalpop  = Population.objects.filter(Q(date_register__year = tinan) & Q(village__id  = userAddress.employee.village.id) & Q(status_datap = 'ac') & Q(type_data = 'f') & Q(id_family = 'i')).count()
    totalpop  = DetailFamily.objects.filter(Q(population__date_register__year = tinan) & Q(population__village__id  = userAddress.employee.village.id) & Q(population__status_datap = 'ac') & Q(population__type_data = 'f') & Q(status = True) & Q(population__id_family = 'i')).count()
    
    totalpopte  = Population.objects.filter(Q(date_register__year = tinan)  & Q(village__id  = userAddress.employee.village.id)  & Q(type_data = 'te')).count()


    context = {
        'title': 'Populasaun Suku',
        'tinan' : tinan,
        'totalpop' : totalpop,
        'totalpopte' : totalpopte,
    }
    return render(request, 'population/dashboard.html', context)





@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def family_list(request):


    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    efamily = ""
    # cek_efamilyautorization = EfamilyActivate.objects.filter(village__id =  userAddress.employee.village.id).count()
    # efamily = cek_efamilyautorization
    totalmembru =  DetailFamily.objects.values('family').filter(Q(population__village__id = userAddress.employee.village.id)).annotate(total=Count('family')).order_by('family')
    family_list = Family.objects.filter(Q(village = userAddress.employee.village.id)).order_by('-id_family')
    

    
    lista_familia = []
    membru = "Dadus Laiha (0)"

    for dados in family_list.iterator():
        totalmembru =  DetailFamily.objects.filter(Q(family__id_family = dados.id_family) & Q(population__village__id = userAddress.employee.village.id)).count()
        pessoa =  DetailFamily.objects.filter(Q(family__id_family = dados.id_family) & Q(population__village__id = userAddress.employee.village.id))
        membru = ""
        for data in pessoa.iterator():

            nu_bi = ""
            nu_e = ""
            nu_p = ""

            if data.population.nu_bi is not None :
                if data.population.nu_bi :
                    nu_bi = "Nú BI ( "+ data.population.nu_bi +")"

            if data.population.nu_e is not None :
                if data.population.nu_e :
                    nu_e = "Nú Eleitoral ( "+ data.population.nu_e +")"

            if data.population.nu_p is not None :
                if data.population.nu_p :
                    nu_p = "Nú Pasaporte ( "+ data.population.nu_p +")"

            membru = membru + data.family_position.name + " " + data.population.name + " " + nu_bi + " " + nu_e +" "+ nu_p 
        if membru == "" :
            membru = "Dadus Laiha (0)"

        lista_familia.append({
            'id_family' : dados.id_family,
            'aldeia' : dados.aldeia,
            'data_registu' : dados.data_registu,
            'total' : totalmembru,
            'hashed' : dados.hashed,
            'membru' : membru  ,
        })





    # family_list = Family.objects.filter(Q(village = userAddress.employee.village.id))


    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Populasaun Suku',
        # 'family_list' : family_list,
        'lista_familia' : lista_familia,
        'total_family' : len(lista_familia),
        'efamily' : efamily,
    }
    return render(request, 'population/population/family_list.html', context)





@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def family_input(request):

    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    
    idfamilia = getnewidf()
    idfmlast = 0

    try:
        fotilastid = Family.objects.filter(village__id = userAddress.employee.village.id).latest('id_family')
        idfmlast = str(fotilastid)
    except Family.DoesNotExist:
        idfmlast = 0 

    lastidfam = int(idfmlast) + 1 
  


    if request.POST :

        id = getlastid_kinos(Family,str(userAddress.employee.village.id))
        hashid = hash_md5(str(id))



        village = Village.objects.get(id=userAddress.employee.village.id)
        dataagora = timezone.now()
        form = Family_form(userAddress.employee.village.id,request.POST)

        if form.is_valid() :
            cek = Family.objects.filter(Q(id_family = request.POST['id_family']) & Q(village__id = userAddress.employee.village.id)).count()
            if cek > 0 :
                messages.error(request,"Rejistu Falla Uma kain ho id : ( " +request.POST['id_family'] + " )  Rejistradu Ona")
            else : 
                instance = form.save(commit=False)
                instance.id = id
                instance.user_created = request.user
                instance.date_created = dataagora
                instance.hashed = hashid
                instance.fdescription = "---"
                instance.municipality = Municipality.objects.get(pk = userAddress.employee.municipality.id)
                instance.administrativepost = AdministrativePost.objects.get(pk =userAddress.employee.administrativepost.id) 
                instance.village = Village.objects.get(pk = userAddress.employee.village.id)  

                instance.save()
                messages.success(request,'Dadus Rejistu Ho susesu !')
            return redirect('population:reg_population')
    else :
        
        form = Family_form(userAddress.employee.village.id)
        context = {
            'lastidfam' : lastidfam,
            'title': 'Populasaun Suku',
            'form' : form ,
            'action' : 'input'

            }
        return render(request, 'population/population/family_input.html', context)



@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def family_edit(request, hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    edit = Family.objects.get(hashed = hashed)
    form = Family_form(userAddress.employee.village.id,instance=edit)
    if request.POST:
        form = Family_form(userAddress.employee.village.id,request.POST, instance=edit)
        if form.is_valid():
            getidfam = Family.objects.get(hashed = hashed)
            if str(getidfam.id_family) == str(request.POST['id_family']) :
                form.save()
                messages.success(request,'Dadus Atualiza Ona Ho susesu !') 
            else : 
                cek = Family.objects.filter(Q(id_family = request.POST['id_family']) & Q(village__id = userAddress.employee.village.id)).count()
                if cek > 0 :
                    messages.error(request,"Atualiza dadus Falla , favor Prenxe id seluk tamba id   : ( " +request.POST['id_family'] + " ) Utuiliza Ona Husi Uma Kain seluk")
                else :
                    cekmember = DetailFamily.objects.filter(Q(family = request.POST['id_family']) & Q(population__village__id = userAddress.employee.village.id)).count()
                    if cekmember > 0 : 
                        messages.success(request,"Familia Ida Ne'e iha ona membru , Sistema La autoriza Atu atualiza dadus !")
                    else :
                         messages.success(request,'Dadus Atualiza Ona Ho susesu !')
                         form.save()
            return redirect('population:reg_population')
    context = {
            'title': 'Populasaun Suku',
            'form' : form ,
            'action' : 'edit'
    }
    return render(request, 'population/population/family_input.html', context)







@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def family_delete(request, hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    dfam = Family.objects.get(hashed = hashed)
    total = DetailFamily.objects.filter(Q(family = dfam.id) & Q(population__village__id = userAddress.employee.village.id)).count()
    if total > 0 :
        messages.error(request,"Apaga Uluk Membru Familia sira , Molok apaga dadus familia ida ne'e !") 
    else :
        Family.objects.filter(Q(hashed = hashed) & Q(village__id = userAddress.employee.village.id)).delete()
        messages.success(request,'Dadus Apaga Ho susesu !')
    return redirect('population:reg_population')







@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def detailfamily_list(request,hashed):

    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    form = CustumDetailFamily_form(userAddress.employee.village.id)
    # Prosesu aumenta membru familia   bazeia  ba dados anterior. wainhira iha request post husi formulario input ne'ebe localiza iha pajina lista membru familia
    if request.POST :
        _, newidf = getlastid(DetailFamily)
        
        idf = str(userAddress.employee.village.id)+str(newidf) 
        hashidf = hash_md5(str(newidf))
        dataagora = timezone.now()
        form = CustumDetailFamily_form(userAddress.employee.village.id,request.POST)
        if form.is_valid():
            familiaid = Family.objects.get(Q(hashed=hashed) & Q(village__id = userAddress.employee.village.id))
            populasaun = DetailFamily.objects.filter(Q(population = request.POST['population']) & Q(status = True) & Q(family__hashed = hashed) & Q(population__village__id = userAddress.employee.village.id)).count()

            if populasaun > 0 :
                messages.error(request,"Populasaun ne'ebe hili . Rejistu ona iha uma kain!")
                return redirect('detailfamily_list', hashed = hashed)
            else :
                pop = Population.objects.get(Q(id = request.POST['population']) & Q(village__id = userAddress.employee.village.id))                    
            
                instance2 = form.save(commit=False)
                instance2.id = idf
                instance2.user_created = request.user
                instance2.family = familiaid
                instance2.date_created = dataagora
                instance2.status_datadp = True
                instance2.hashed = hashidf
                instance2.save()


                populasaun = get_object_or_404(Population, id= pop.id)
                populasaun.id_family = 'i'
                populasaun.save() 
                messages.success(request,"Dadus Rejistu Ho susesu !")
                return redirect('population:detailfamily_list', hashed = hashed)

    
    familia = Family.objects.get(Q(hashed=hashed) & Q(village__id = userAddress.employee.village.id))
    familymember_list = DetailFamily.objects.filter(Q(family = familia) & Q(population__village__id = userAddress.employee.village.id)).order_by("family_position__id")
    total_ativu = DetailFamily.objects.filter(Q(family = familia) & Q(status = True) & Q(population__village__id = userAddress.employee.village.id)).count()
    total_desativu = DetailFamily.objects.filter(Q(family = familia) & Q(status = False) & Q(population__village__id = userAddress.employee.village.id)).count()
    check_chefe = DetailFamily.objects.filter(Q(family_position = 1) & Q(family = familia.id)  & Q(status = True) & Q(population__village__id = userAddress.employee.village.id)).count()

    family_member = []
    # rekola dados hotu husi membru familia idak- idak hodi haruka ba interface
    for dados in familymember_list.iterator():
        data_migrasaun = "laiha"
        deskrisaunm = "laiha"
        migrasaun_husi = "laiha"
        #karik membru familia nee popukasaun migrasaun entao foti nia dados
        if dados.population.type_data == 'm' :

            # print("-----------------migarasaun---------------")
            try:
                infom = Migration.objects.get(population = dados.population.id)
                data_migrasaun = infom.date_migration
                deskrisaunm = infom.descriptionm

                if infom.cidadaunm.id == 1 :
                    migrasaun_husi = infom.from_aldeia.name + " / " + infom.from_aldeia.village.name + " / " + infom.from_aldeia.village.administrativepost.name + " / " + infom.from_aldeia.village.administrativepost.municipality.name

                elif infom.cidadaunm.id == 2 :
                    migrasaun_husi = infom.cidadaunm.name
                else :
                    print("Sedauk iha")

            except Migration.DoesNotExist:
                dekrisaunmate = 'laiha'
                datamate = 'laiha'
            print(migrasaun_husi)

        # foti dados mate husi populasaun nia karik iha
        try:
            mate = Death.objects.get(population = dados.population.id)
            dekrisaunmate = mate.descriptiond
            datamate = mate.date
        except Death.DoesNotExist:
            dekrisaunmate = 'laiha'
            datamate = 'laiha'

        # foti dados mudansa  husi populasaun nia karik iha
        try:
            sai = Migrationout.objects.get(population = dados.population.id)
            dekrisaunsai = sai.descriptionmo
            datasai = sai.date_migration
        except Migrationout.DoesNotExist:
            dekrisaunsai = 'laiha'
            datasai = 'laiha'
        
        try:
            change = ChangeFamily.objects.get(familymember = dados.id)
            dekrisauncf = change.descriptioncf
            datacf = change.date_change
            hashedcf = change.hashed
            idfam = DetailFamily.objects.get(id = dados.id)
            cek = DetailFamily.objects.filter(Q(population = idfam.population) &  Q(population__village__id  = userAddress.employee.village.id))
            last_family = ""
            for data in cek.iterator() :
                last_family = data.family.hashed

        except ChangeFamily.DoesNotExist:
            dekrisauncf = 'laiha'
            datacf = 'laiha'
            last_family = ''

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





        #  input dados no informasaun nian ba iha array husdi haruka ba iha interface membru
        family_member.append({
            'family_position' : dados.family_position,
            'status' : dados.status,
            'data_migrasaun' : data_migrasaun,
            'deskrisaunm' : deskrisaunm,
            'migrasaun_husi' : migrasaun_husi,
            'dekrisaunmate' : dekrisaunmate,
            'datamate' : datamate,
            'dekrisaunsai' : dekrisaunsai,
            'datasai' : datasai,
            'id': dados.population.id,
            'hashed' : dados.hashed,
            'village': dados.population.village, 
            'aldeia': dados.population.aldeia, 
            'profession': dados.population.profession,
            'date_register': dados.population.date_register,
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
            'date_created': dados.population.date_register,
            'dekrisauncf' : dekrisauncf,
            'datacf' : datacf,
            'last_family' : last_family,
            'lingua': "Lingua Internasional :  " + linguadata + " , Lingua Materna : " + linguamaterna,
            'nu_e': dados.population.nu_e,
            'nu_p': dados.population.nu_p,
            'kondisaun': dados.population.deficient,
            'phone': dados.population.phone,
            'vulnerable': dados.population.vulnerable,
            })



    context = {
        'check_chefe' : check_chefe,
        'total_desativu' : total_desativu,
        'total_ativu' : total_ativu,
        'title': 'Detallu familia',
        'familymember_list' : familymember_list,
        'hashed' : hashed,
        'form' : form,
        'family_member' : family_member,
        'id_familia' : f"{familia.id_family:010}",
        'total_family' : len(familymember_list),
    }
    return render(request, 'population/population/detailfamily_list.html', context)








@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def familymember_input(request, hashed):

    munisipiu = Municipality.objects.all()
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    familiaid = Family.objects.get(hashed=hashed)

    if request.POST :

        # _, newid = getlastid(Population)
        # # id = str(userAddress.employee.village.id)+str(newid) 
        # id = newid
        # hashid = hash_md5(str(newid))



        id = getlastid_kinos(Population,str(userAddress.employee.village.id))
        hashid = hash_md5(str(id))


        # _, newidf = getlastid(DetailFamily)
        # # idf = str(userAddress.employee.village.id)+str(newidf) 
        # idf = newidf
        # hashidf = hash_md5(str(newidf))

        # idf = getlastid_kinos_df(DetailFamily,str(userAddress.employee.village.id))
        # hashidf = hash_md5(str(idf))

        idf = getlastid_kinosrp(DetailFamily,str(userAddress.employee.village.id))
        hashidf = hash_md5(str(idf))



    

        # _, newidm = getlastid(Migration)
        # # idm = str(userAddress.employee.village.id)+str(newidm) 
        # idm = newidm
        # hashidm = hash_md5(str(newidm))

        idm = getlastid_kinos(Migration,str(userAddress.employee.village.id))
        hashidm = hash_md5(str(idm))
    


        village = Village.objects.get(id=userAddress.employee.village.id)
        userid = User.objects.get(id=request.user.id)


        dataagora = timezone.now()
        form = Population_form(userAddress.employee.village.id,request.POST,request.FILES)
        formdf = DetailFamily_form(request.POST)

        if form.is_valid() & formdf.is_valid() :

            instance = form.save(commit=False)
            instance.id = id
            instance.id_family = 'i'
            instance.user_created = userid
            instance.date_created = dataagora
            instance.hashed = hashid

            if request.POST['type_data'] == "popsuku" :
                instance.type_data = "f"
                instance.date_register = request.POST['date_register']

            elif request.POST['type_data'] == "formmigration" :
                instance.type_data = "m"
                instance.date_register = request.POST['date_migration']
            
            if request.POST['cidadaunm'] == '1' or request.POST['cidadaunm'] == '2' :
                instance.nationality = request.POST['cidadaunm']
            else :
                instance.nationality = '1'

            instance.unique_id = "33"
            instance.municipality = Municipality.objects.get(pk = userAddress.employee.municipality.id)
            instance.administrativepost = AdministrativePost.objects.get(pk =userAddress.employee.administrativepost.id) 
            instance.village = Village.objects.get(pk = userAddress.employee.village.id)  
            instance.status_datap = "ac"


            instance.save()

            populasaun = Population.objects.get(id = id)
            family_position = FamilyPosition.objects.get(id = request.POST['family_position'])

            instance2 = formdf.save(commit=False)
            instance2.id = idf
            instance2.user_created = userid
            instance2.family = familiaid
            instance2.population = populasaun
            instance2.family_position = family_position
            instance2.date_created = dataagora
            instance2.status_datadp = True
            instance2.hashed = hashidf
            instance2.save()

#id,village,population,user_created,descriptionm,date_created,hashed

            if request.POST['type_data'] == "formmigration" :
                formm = Migration_form(request.POST)
        
                if formm.is_valid() :
                    instance3 = formm.save(commit=False)
                    instance3.id = idm
                    instance3.village = village
                    instance3.descriptionm = request.POST['descriptionp']
                    instance3.population = populasaun
                    instance3.date_created = dataagora
                    instance3.user_created = userid
                    instance3.hashed = hashidm
                    instance3.save()


            messages.success(request,'Dadus Rejistu Ho susesu !')
            return redirect('population:detailfamily_list', hashed = hashed)

    else :
        
        form = Population_form(userAddress.employee.village.id)
        formdf = DetailFamily_form()
        formm = Migration_form()


        context = {
            'title': 'Rejistu Membru Família',
            'form' : form ,
            'munisipiu' : munisipiu,
            'hashed' : hashed,
            'formdf' : formdf ,
            'formm' : formm,
            'prosses' : 'registu',
            }
        return render(request, 'population/population/familymember_input.html', context)






@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def familymember_update(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    detailfamdata = DetailFamily.objects.get(hashed = hashed)
    pophash = Population.objects.get(id = detailfamdata.population.id)
    famhash = Family.objects.get(id = detailfamdata.family.id)
    prosses = "edit_pop"
    formm =  Migration_form()

    if pophash.type_data == 'm':
        print("tamaaaaaaaaaaaaaa")
        migrationdata = Migration.objects.get(population = pophash.id)
        formm = Migration_form(instance = migrationdata )
        prosses = 'edit_mig'
    form = Population_form(userAddress.employee.village.id,instance=pophash)
    formdf = DetailFamily_form(instance=detailfamdata)

    if request.POST :
        form = Population_form(userAddress.employee.village.id,request.POST,request.FILES, instance=pophash)
        formdf = DetailFamily_form(request.POST, instance=detailfamdata)
        if form.is_valid() & formdf.is_valid() :
            instance = form.save(commit=False)

            if request.POST['type_data'] == "popsuku" :
                instance.date_register = request.POST['date_register']

            elif request.POST['type_data'] == "formmigration" :
                instance.date_register = request.POST['date_migration']

            if request.POST['type_data'] == "formmigration" :
                formm = Migration_form(request.POST, instance=migrationdata)
                if formm.is_valid():
                    formm.save()
                    instance.nationality = request.POST['cidadaunm'] 
            instance.save()
            formdf.save()
        messages.success(request,'Dadus Atualiza Ho susesu !')
        return redirect('population:detailfamily_list', hashed = famhash.hashed)
    
    context = {

        'title': 'Atualiza Dadus Populasaun',
        'form' : form ,
        'formdf' : formdf ,
        'hashed' : hashed,
        'formm' : formm,
        'prosses' : prosses,

        }
    return render(request, 'population/population/familymember_input.html', context)




@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def familymember_updateep(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    detailfamdata = DetailFamily.objects.get(hashed = hashed)
    pophash = Population.objects.get(id = detailfamdata.population.id)
    famhash = Family.objects.get(id = detailfamdata.family.id)

    longuamat = "";

    if pophash.language != None :
        datalingua = pophash.language
        datalingua = datalingua.split('*#')
        longuamat = datalingua[1]
        datalingua = datalingua[0]
        datalingua = datalingua.split('-')

        print("kokooko")
        print(longuamat)



    else : 
        datalingua = "ko"
  
    lingualop = []
    language = Language.objects.all()
    for dadoslingua in language : 
        if str(dadoslingua.id) in datalingua :
            lingualop.append({'id':dadoslingua.id,'name' : dadoslingua.name,'hili' : "yes" }) 
        else :
            lingualop.append({'id':dadoslingua.id,'name' : dadoslingua.name,'hili' : "no" }) 


    form = Population2_form(instance=pophash)


    if request.POST :
        koko = request.POST.getlist('lingua')
       
        idlingua = "-"

        for data in koko :
            idlingua = idlingua + data[0] + "-" 





       


        form = Population2_form(request.POST, instance=pophash)
       
        if form.is_valid():
            instance = form.save(commit=False)
            instance.language = idlingua + " *# " + request.POST['lingua_materna']
            instance.save()
  
        messages.success(request,'Dadus Update Ho susesu !')
        return redirect('population:detailfamily_list', hashed = famhash.hashed)
    
    context = {

        'title': 'Atualiza Dadus Populasaun',
        'form' : form ,
        'hashed' : hashed,
        'longuamat' : longuamat,
        'language' : lingualop,
        'poplang' : datalingua,
        'datalingua' : datalingua,

        }
    return render(request, 'population/population/familymember_input.html', context)



@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def familymember_mudasuku(request,hashed):
    return redirect('detailfamily_list', hashed = hashed)



@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def familymember_delete(request, hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    dfam = DetailFamily.objects.get(hashed = hashed)
    populasaun = dfam.population.id
    # cek pesoa ne'e hola parte ona iha familia seluk ka lae
    total = DetailFamily.objects.filter(Q(population = populasaun) & Q(population__village__id = userAddress.employee.village.id )).count()

    # karik iha apaga pesoa nia dados ne'ebe liga ho familia iha ne'ebe apaga
    if total > 1 :
        DetailFamily.objects.filter(Q(id = dfam.id) & Q(population__village__id = userAddress.employee.village.id)).delete()
        populasaun = get_object_or_404(Population, id= populasaun)
        populasaun.id_family = 'l'
        populasaun.save()
    else :
    #karik laiha apaga dados populasaun nia husi database
        Population.objects.filter(Q(id = populasaun) & Q(village__id = userAddress.employee.village.id)).delete()
    messages.success(request,'Dadus Apaga Ho susesu !')
    return redirect('population:detailfamily_list', hashed = dfam.family.hashed)




@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def familymember_out(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    village = Village.objects.get(id= userAddress.employee.village.id)
    dataagora = timezone.now()

    detailfamdata = DetailFamily.objects.get(hashed = hashed)
    pophash = Population.objects.get(id = detailfamdata.population.id)
  
    cek_dadosmate = Migrationout.objects.filter(Q(population = detailfamdata.population.id) & Q(population__village__id = userAddress.employee.village.id))

    familiaid = Family.objects.get(id=detailfamdata.family.id)

    form = Migrationout_form(userAddress.employee.village.id)
    prosses = "input"
    if len(cek_dadosmate) > 0 :
        datamate = Migrationout.objects.get(population = detailfamdata.population.id)
        form = Migrationout_form(userAddress.employee.village.id,instance=datamate)
        prosses = "edit"

    if request.POST :
        if request.POST['prosses'] == 'input' :
            # _, newidd = getlastid(Migrationout)
            # idd = str(userAddress.employee.village.id)+str(newidd) 
            # idd = newidd

            idd = getlastid_kinos(Migrationout,str(userAddress.employee.village.id))
            hashid = hash_md5(str(idd))


            # hashid = hash_md5(str(newidd))


            form = Migrationout_form(userAddress.employee.village.id,request.POST)
            cekmuda = Migrationout.objects.filter(population=pophash.id).count()
            if cekmuda == 0 :
                if form.is_valid() :
                    instance = form.save(commit=False)
                    instance.id = idd
                    instance.population = pophash
                    instance.user_created = request.user
                    instance.date_created = dataagora
                    instance.hashed = hashid
                    instance.village = village
                    instance.save()
                    
                    populasaun = get_object_or_404(Population, id= detailfamdata.population.id)
                    populasaun.status_datap = 'mu'
                    populasaun.save()

                    dfam = get_object_or_404(DetailFamily, id= detailfamdata.id)
                    dfam.status = False
                    dfam.save()
                    messages.success(request,'Dadus Rejitu Ho susesu !')
                    return redirect('population:detailfamily_list', hashed = familiaid.hashed)
            else :
                return redirect('population:detailfamily_list', hashed = familiaid.hashed)

        elif request.POST['prosses'] == 'edit' :
            datamate = Migrationout.objects.get(population = detailfamdata.population.id)
            form = Migrationout_form(userAddress.employee.village.id,request.POST,instance = datamate)
            if form.is_valid() :
                form.save()
                messages.success(request,'Dadus Atualiza Ho susesu !')
                return redirect('population:detailfamily_list', hashed = familiaid.hashed)
    context = {
        'title': 'Populasaun sai',
        'form' : form ,
        'prosses' : prosses,
        'name' : pophash.name
        }
    return render(request, 'population/population/familymember_out.html', context)








@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def familymember_mate(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    village = Village.objects.get(id=userAddress.employee.village.id)
    dataagora = timezone.now()

    detailfamdata = DetailFamily.objects.get(hashed = hashed)
    pophash = Population.objects.get(id = detailfamdata.population.id)
  
    cek_dadosmate = Death.objects.filter(Q(population = detailfamdata.population.id) & Q(population__village__id =  userAddress.employee.village.id ))

    familiaid = Family.objects.get(id=detailfamdata.family.id)

    form = Death_form()
    prosses = "input"
    if len(cek_dadosmate) > 0 :
        datamate = Death.objects.get(population = detailfamdata.population.id)
        form = Death_form(instance=datamate)
        prosses = "edit"

    if request.POST :
        if request.POST['prosses'] == 'input' :


            # _, newidd = getlastid(Death)
            # idd = str(userAddress.employee.village.id)+str(newidd) 
            # idd = newidd

            idd = getlastid_kinos(Death,str(userAddress.employee.village.id))
            hashid = hash_md5(str(idd))

            # hashid = hash_md5(str(newidd))
            form = Death_form(request.POST)

            cekmate = Death.objects.filter(population=pophash.id).count()

            if cekmate == 0 :
                if form.is_valid() :
                    instance = form.save(commit=False)
                    instance.id = idd
                    instance.population = pophash
                    instance.user_created = request.user
                    instance.date_created = dataagora
                    instance.hashed = hashid
                    instance.village = village
                    instance.save()

                    populasaun = get_object_or_404(Population, id= detailfamdata.population.id)
                    populasaun.status_datap = 'ma'
                    populasaun.save()

                    dfam = get_object_or_404(DetailFamily, id= detailfamdata.id)
                    dfam.status = False
                    dfam.save()

                    messages.success(request,'Dadus Rejitu Ho susesu !')
                    return redirect('population:detailfamily_list', hashed = familiaid.hashed)
            else : 
                    return redirect('population:detailfamily_list', hashed = familiaid.hashed)


        elif request.POST['prosses'] == 'edit' :
            datamate = Death.objects.get(population = detailfamdata.population.id)
            form = Death_form(request.POST,instance = datamate)
            if form.is_valid() :
                form.save()
                messages.success(request,'Dadus Atualiza Ho susesu !')
                return redirect('population:detailfamily_list', hashed = familiaid.hashed)

    context = {
        'title': 'Populasaun Death',
        'form' : form ,
        'prosses' : prosses,
        'name' : pophash.name,
        }
    return render(request, 'population/population/familymember_death.html', context)




@login_required
@allowed_users(allowed_roles=['sec','xefe'])
def familymember_change(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    village = Village.objects.get(id=userAddress.employee.village.id)
    dataagora = timezone.now()

    detailfamdata = DetailFamily.objects.get(hashed = hashed)
   
    cek_dados = ChangeFamily.objects.filter(familymember = detailfamdata.id)

    familiaid = Family.objects.get(id=detailfamdata.family.id)

    form = Changefamily_form()
    prosses = "input"
    if len(cek_dados) > 0 :
        dados = ChangeFamily.objects.get(familymember = detailfamdata.id)
        form = Changefamily_form(instance=dados)
        prosses = "edit"

    if request.POST :
        if request.POST['prosses'] == 'input' :
            # _, newidd = getlastid(ChangeFamily)
            # idc = str(userAddress.employee.village.id)+str(newidd) 
            # idc = newidd

            idc = getlastid_kinos(ChangeFamily,str(userAddress.employee.village.id))
            hashid = hash_md5(str(idc))


            # hashid = hash_md5(str(newidd))

            form = Changefamily_form(request.POST)

            if form.is_valid() :
                instance = form.save(commit=False)
                instance.id = idc
                instance.familymember = detailfamdata
                instance.user_created = request.user
                instance.date_created = dataagora
                instance.hashed = hashid
                instance.village = village
                instance.save()

                populasaun = get_object_or_404(Population, id= detailfamdata.population.id)
                populasaun.id_family = 'l'
                populasaun.save()

                dfam = get_object_or_404(DetailFamily, id= detailfamdata.id)
                dfam.status = False
                dfam.save()

                messages.success(request,'Dadus Rejitu Ho susesu !')
                return redirect('population:detailfamily_list', hashed = familiaid.hashed)

        elif request.POST['prosses'] == 'edit' :
            datac = ChangeFamily.objects.get(familymember = detailfamdata.id)
            form = Changefamily_form(request.POST,instance = datac)
            if form.is_valid() :
                form.save()
                messages.success(request,'Dadus Atualiza Ho susesu !')
                return redirect('population:detailfamily_list', hashed = familiaid.hashed)

    context = {
        'title': 'Populasaun Death',
        'form' : form ,
        'prosses' : prosses,
        'name' : detailfamdata.population.name,
        }
    return render(request, 'population/population/familymember_change.html', context)



def familymember_mate_apaga(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    dfamily = DetailFamily.objects.get(hashed = hashed)
    Death.objects.filter(Q(population=dfamily.population) & Q(population__village__id = userAddress.employee.village.id)).delete()
    populasaun = get_object_or_404(Population, id= dfamily.population.id)
    populasaun.status_datap = 'ac'
    populasaun.save()

    dfam = get_object_or_404(DetailFamily, id= dfamily.id)
    dfam.status = True
    dfam.save()

    messages.success(request,'Dadus Apaga Ho susesu !')
    return redirect('population:detailfamily_list', hashed = dfamily.family.hashed)


def familymember_out_apaga(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    dfamily = DetailFamily.objects.get(hashed = hashed)
    Migrationout.objects.filter(Q(population=dfamily.population) & Q(population__village__id = userAddress.employee.village.id)).delete()

    populasaun = get_object_or_404(Population, id= dfamily.population.id)
    populasaun.status_datap = 'ac'
    populasaun.save()


    dfam = get_object_or_404(DetailFamily, id= dfamily.id)
    dfam.status = True
    dfam.save()

    messages.success(request,'Dadus Apaga Ho susesu !')
    return redirect('population:detailfamily_list', hashed = dfamily.family.hashed)





def familymember_desativu(request,hashed):
    dfamily = DetailFamily.objects.get(hashed = hashed)

    populasaun = get_object_or_404(Population, id= dfamily.population.id)
    populasaun.id_family = 'l'
    populasaun.save()

    dfam = get_object_or_404(DetailFamily, id= dfamily.id)
    dfam.status = False
    dfam.save()
    messages.success(request,'Membru Desativu Ona Husi Familia !')
    return redirect('population:detailfamily_list', hashed = dfamily.family.hashed)

def familymember_ativu(request,hashed):
    dfamily = DetailFamily.objects.get(hashed = hashed)

    populasaun = get_object_or_404(Population, id= dfamily.population.id)
    populasaun.id_family = 'i'
    populasaun.save()

    dfam = get_object_or_404(DetailFamily, id= dfamily.id)
    dfam.status = True
    dfam.save()

    messages.success(request,'Membru Ativu  Ona ho Susesu Familia !')
    return redirect('population:detailfamily_list', hashed = dfamily.family.hashed)







