from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Temporary
from population.utils import getnewidp,getnewidf
from population.forms import Family_form,Family_form,FamilyPosition,Population_form,PopulationTemporary_form,Temporary_form
from django.views.decorators.csrf import csrf_exempt
import json
from population.utils import getlastid_kinos,getlastid_kinosrp

from django.utils import timezone
from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404
from employee.models import *
from django.db.models import Q


@login_required
def temporary_list(request):
    
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    temporary_list = Temporary.objects.filter(village = userAddress.employee.village.id)
    context = {
        'title': 'Temporario Suku',
        'temporary_list' : temporary_list,
        'total_data' : len(temporary_list),
    }
    return render(request, 'population/temporary/temporary_list.html', context)


# id , village,aldeia,profession,citizen,religion,user_created,unique_id,name,date_of_bird,place_of_bird,gender,marital_status,level_education,readalatin,readaarabe,readachina,nu_bi,id_pasaporte,id_family,descriptionp,imagen,status_datap,type_data,date_created,hashed

@login_required
def temporary_input(request):
    
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    if request.POST :



        # _, newid = getlastid(Population)
        # id = str(userAddress.employee.village.id)+str(newid) 
        # id = newid
        # hashid = hash_md5(str(newid))



        # _, newitemp = getlastid(Temporary)
        # idt = str(userAddress.employee.village.id)+str(newitemp) 
        # idt = newitemp
        # hashidt = hash_md5(str(newitemp))



        newid = getlastid_kinos(Population,str(userAddress.employee.village.id))
        hashid = hash_md5(str(newid))



        idt = getlastid_kinos(Temporary,str(userAddress.employee.village.id))
        hashidt = hash_md5(str(idt))



    
        village = Village.objects.get(id=userAddress.employee.village.id)
        userid = User.objects.get(id=request.user.id)

        dataagora = timezone.now()

        form = PopulationTemporary_form(userAddress.employee.village.id,request.POST)
        formtemp = Temporary_form(request.POST)


#   ,imagen,

        if form.is_valid() & formtemp.is_valid() : 
            instance = form.save(commit=False)
            instance.id = newid
            instance.id_family = ''
            instance.marital_status = ''
            instance.user_created = userid
            instance.date_created = dataagora
            instance.date_register = request.POST['date_arive']
            instance.hashed = hashid
            instance.descriptionp =''
            instance.readalatin = ''
            instance.readaarabe = ''
            instance.readachina = ''
            instance.type_data = request.POST['type_data']
            instance.unique_id = "33"
            instance.status_datap = 'ac'
            instance.village = village
            instance.save()

            populasaun = Population.objects.get(id = newid)

            instance2 = formtemp.save(commit=False)
            instance2.id = idt
            instance2.village = village
            instance2.user_created = userid
            instance2.population = populasaun
            instance2.date_created = dataagora
            instance2.hashed = hashidt
            instance2.save()
            
            return redirect('population:temporary')
    else :
        print("tama")
        
        form = PopulationTemporary_form(userAddress.employee.village.id)
        formtemp = Temporary_form()

        context = {
            'title': 'Populasaun Temporáriu',
            'form' : form ,
            'prosses' : "input",
            'titlebutton' : "Registu",
            'formtemp' : formtemp,
            'title' : "Rejistu Populasaun Temporáriu"
            }
        return render(request, 'population/temporary/temporary_input.html', context)




@login_required
def temporary_update(request,hashed):
    
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)

    temp = Temporary.objects.get(hashed = hashed)
    pop = Population.objects.get(id = temp.population.id)
    form = PopulationTemporary_form(userAddress.employee.village.id,instance=pop)
    formtemp = Temporary_form(instance=temp)

    if request.POST :
        form = PopulationTemporary_form(userAddress.employee.village.id,request.POST,instance=pop)
        formtemp = Temporary_form(request.POST, instance=temp)
        if form.is_valid() & formtemp.is_valid() :
            instance = form.save(commit=False)
            instance.date_register = request.POST['date_arive']
            instance.save()
            formtemp.save()
            return redirect('population:temporary')
    
    context = {
        'title': 'Populasaun Temporáriu',
        'form' : form ,
        'prosses' : pop.type_data,
        'formtemp' : formtemp,
        'titlebutton' : "Atualiza",
        'title' : "Atualiza Dadus Populasaun Temporáriu"
        }
    return render(request, 'population/temporary/temporary_input.html', context)



@login_required
def temporary_delete(request,hashed):
    
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)


    Temporary.objects.filter(Q(hashed=hashed) & Q(population__village__id=userAddress.employee.village.id)).delete()
    messages.success(request,'Dadus Apaga Ho susesu !')
    return redirect('population:temporary')