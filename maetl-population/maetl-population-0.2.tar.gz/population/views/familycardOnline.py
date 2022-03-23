from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Temporary,ChangeFamily,FamilyCardOnline
from population.utils import getnewidp,getnewidf
from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,CustumDetailFamily_form,Death_form,Migration_form,Migrationout_form,Changefamily_form
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

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView


@login_required
def familycard_list(request):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    totalmembru =  DetailFamily.objects.values('family').filter(Q(population__village__id = userAddress.employee.village.id)).annotate(total=Count('family')).order_by('family')
    family_list = Family.objects.filter(Q(village = userAddress.employee.village.id)).order_by('-id_family')
    lista_familia = []
    membru = "Dados Laiha (0)"

    for dados in family_list.iterator():
        totalmembru =  DetailFamily.objects.filter(Q(family__id_family = dados.id_family) & Q(population__village__id = userAddress.employee.village.id)).count()

        familycard = dados.id_family
        koko = str(userAddress.employee.village.id) + str(f"{familycard:010}")
        print("--------------") 
        print(koko)
        card = "laiha"
        famusername = "laiha"

        cardcount = User.objects.filter(username=koko).count()
        if cardcount > 0 :
            datausername = FamilyCardOnline.objects.get(user__username=koko)
            famusername = datausername.user.username
            card = "iha"
        else : 
            card = "laiha"
        
     

        pessoa =  DetailFamily.objects.filter(Q(family__id_family = dados.id_family) & Q(population__village__id = userAddress.employee.village.id))
        membru = ""

        for data in pessoa.iterator():
            membru = membru + data.family_position.name + " " + data.population.name + "Nu. BI (" + data.population.nu_bi + ") " 
        if membru == "" :
            membru = "Dados Laiha (0)"

        lista_familia.append({
            'id_family' : dados.id_family,
            'aldeia' : dados.aldeia,
            'data_registu' : dados.data_registu,
            'total' : totalmembru,
            'hashed' : dados.hashed,
            'membru' : membru  ,
            'cardx' : card ,
            'famusername' : famusername,
        })

    family_list = Family.objects.filter(Q(village = userAddress.employee.village.id))
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Populasaun Suku',
        'family_list' : family_list,
        'lista_familia' : lista_familia,
        'total_family' : len(family_list),

    }
    return render(request, 'population/familycard_online/familycard_list.html', context)



@login_required
def registerfamilycard(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    form = CustumDetailFamily_form(userAddress.employee.village.id)
    # Prosesu aumenta membru familia   bazeia  ba dados anterior. wainhira iha request post husi formulario input ne'ebe localiza iha pajina lista membru familia
    if request.POST :
        
        xx = int(request.POST['id_familia'])
        kord = request.POST['kordinate']
        kord2 = kord.replace("LatLng(", "")
        kord2 = kord2.replace(")", "")

        koko = str(userAddress.employee.village.id)+str(f"{xx:010}") 
        first_name = str(userAddress.employee.village.id)+"F"+str(f"{xx:010}") 
      
        password = make_password('vixafamilia')
        obj2 = User(username=koko, password=password,first_name=first_name,last_name='familycard20521693')
        obj2.save()


        _, newidf = getlastid(FamilyCardOnline)
        hashid = hash_md5(str(newidf))

        iduser = User.objects.get(username=koko)
        obj3 = FamilyCardOnline(
            village = Village.objects.get(id =userAddress.employee.village.id),
            administrativepost = AdministrativePost.objects.get(id=userAddress.employee.village.administrativepost.id),
            municipality = Municipality.objects.get(id=userAddress.employee.village.administrativepost.municipality.id),
            user = iduser,
            date_created =   timezone.now(),
            family=Family.objects.get(Q(id_family =  request.POST['id_familia']) & Q(village = userAddress.employee.village.id )),
            cordinate = kord2,
            user_created = request.user.id,
            hashed = hashid,
            )
        obj3.save()



        messages.success(request,"Konta kria Ho susesu !")
        return redirect('population:familycard_list')

    
    familia = Family.objects.get(Q(hashed=hashed) & Q(village__id = userAddress.employee.village.id))
    


    context = {
        'id_familia' : familia.id_family,
    }
    return render(request, 'population/familycard_online/registerfamilycard.html', context)




@login_required
def updatefamilycard(request,hashed):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    form = CustumDetailFamily_form(userAddress.employee.village.id)
    # Prosesu aumenta membru familia   bazeia  ba dados anterior. wainhira iha request post husi formulario input ne'ebe localiza iha pajina lista membru familia
    if request.POST :
        xx = int(request.POST['id_familia'])
        kord = request.POST['kordinate']
        kord2 = kord.replace("LatLng(", "")
        kord2 = kord2.replace(")", "")

        familia = Family.objects.get(Q(hashed=hashed) & Q(village__id = userAddress.employee.village.id))

        FamilyCardOnline.objects.filter(family=familia.id).update(cordinate=kord2)
        

        messages.success(request,"Localizasaun Atualiza ho susesu !")
        return redirect('population:familycard_list')

    
    familia = Family.objects.get(Q(hashed=hashed) & Q(village__id = userAddress.employee.village.id))

    kordinate = FamilyCardOnline.objects.get(Q(family = familia.id) & Q(village__id = userAddress.employee.village.id))
    


    context = {
        'id_familia' : familia.id_family,
        'kordinate' : kordinate.cordinate,
    }
    return render(request, 'population/familycard_online/updatefamilycard.html', context)


@login_required
def resetpassword(request,hashed):

    if request.POST :
        userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
        familia = Family.objects.get(Q(hashed=hashed) & Q(village__id = userAddress.employee.village.id))

        koko = str(userAddress.employee.village.id)+str(f"{familia.id_family:010}") 

        User.objects.filter(username=koko).update(password=make_password(request.POST['password']))

        messages.success(request,"Password Troka Susesu")
        return redirect('population:familycard_list')
    context = {
        'title' : "Troka Password",
    }
    return render(request, 'population/familycard_online/newpasswordfamilycard.html', context)

    



