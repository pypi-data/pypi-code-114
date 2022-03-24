from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,AdministrativePost,Level_Education,Temporary
from population.utils import getnewidp,getnewidf
from population.forms import Family_form,Family_form,Citizen_form,FamilyPosition,Municipality,Population_form,Aldeia_form,DetailFamily_form,Village_form,CustumDetailFamily_form,Death_form,Migration_form,Migrationout_form,Citizen_form,Religion_form,Level_Education_form,Profession_form,AdministrativePost_form,Municipality_form,FamilyPosition_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q








@login_required
def municipality_list(request):
    municipality_list = Municipality.objects.all()
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Munisipiu',
        'municipality_list' : municipality_list,
        'total_dados' : len(municipality_list)
    }
    return render(request,'population/custom/municipality/municipality_list.html',context)



@login_required
def municipality_input(request):
    if request.POST :
        form = Municipality_form(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Registu Ho susesu !')
            return redirect('population:municipality')
        else : 
            messages.error(request,'Dados Prenxe Lalos Ou eziste Ona')
            return redirect('population:municipality')
    else :
        
        form = Municipality_form()
        context = {
            'title': 'Registo Dados ',
            'form' : form,
            }
        return render(request, 'population/custom/municipality/municipality_input.html', context)



@login_required
def municipality_edit(request,id):
    getdata = Municipality.objects.get(id = id)
    if request.POST :
        form = Municipality_form(request.POST,instance = getdata)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Update Ho susesu !')
            return redirect('population:municipality')
        else : 
            messages.error(request,'Dados Update Falla')
            return redirect('population:municipality')
    else :
        form = Municipality_form(instance = getdata)
        context = {
            'title': 'Atualiza Dados',
            'form' : form,
            }
        return render(request, 'population/custom/municipality/municipality_input.html', context)


@login_required
def municipality_delete(request,id):
    getdata = Municipality.objects.filter(id = id).delete()
    messages.success(request,'Dados Apaga Ho susesu !')
    return redirect('population:municipality')













@login_required
def administrativepost_list(request):
    administrativepost_list = AdministrativePost.objects.all()
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Postu Administrativo',
        'administrativepost_list' : administrativepost_list,
        'total_dados' : len(administrativepost_list)
    }
    return render(request,'population/custom/administrativepost/administrativepost_list.html',context)



@login_required
def administrativepost_input(request):
    if request.POST :
        form = AdministrativePost_form(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Registu Ho susesu !')
            return redirect('population:administrativepost')
        else : 
            messages.error(request,'Dados Prenxe Lalos Ou eziste Ona')
            return redirect('population:administrativepost')
    else :
        
        form = AdministrativePost_form()
        context = {
            'title': 'Registo Dados ',
            'form' : form,
            }
        return render(request, 'population/custom/administrativepost/administrativepost_input.html', context)



@login_required
def administrativepost_edit(request,id):
    getdata = AdministrativePost.objects.get(id = id)
    if request.POST :
        form = AdministrativePost_form(request.POST,instance = getdata)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Update Ho susesu !')
            return redirect('population:administrativepost')
        else : 
            messages.error(request,'Dados Update Falla')
            return redirect('population:administrativepost')
    else :
        form = AdministrativePost_form(instance = getdata)
        context = {
            'title': 'Atualiza Dados',
            'form' : form,
            }
        return render(request, 'population/custom/administrativepost/administrativepost_input.html', context)


@login_required
def administrativepost_delete(request,id):
    getdata = AdministrativePost.objects.filter(id = id).delete()
    messages.success(request,'Dados Apaga Ho susesu !')
    return redirect('population:administrativepost')










@login_required
def village_list(request):
    village_list = Village.objects.all()
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Village',
        'village_list' : village_list,
        'total_dados' : len(village_list)
    }
    return render(request,'population/custom/village/village_list.html',context)



@login_required
def village_input(request):
    if request.POST :
        form = Village_form(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Registu Ho susesu !')
            return redirect('population:village')
        else : 
            messages.error(request,'Dados Prenxe Lalos Ou eziste Ona')
            return redirect('population:village')
    else :
        
        form = Village_form()
        context = {
            'title': 'Registo Dados ',
            'form' : form,
            }
        return render(request, 'population/custom/village/village_input.html', context)



@login_required
def village_edit(request,id):
    getdata = Village.objects.get(id = id)
    if request.POST :
        form = Village_form(request.POST,instance = getdata)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Update Ho susesu !')
            return redirect('population:village')
        else : 
            messages.error(request,'Dados Update Falla')
            return redirect('population:village')
    else :
        form = Village_form(instance = getdata)
        context = {
            'title': 'Atualiza Dados',
            'form' : form,
            }
        return render(request, 'population/custom/village/village_input.html', context)


@login_required
def village_delete(request,id):
    getdata = Village.objects.filter(id = id).delete()
    messages.success(request,'Dados Apaga Ho susesu !')
    return redirect('population:village')













@login_required
def aldeia_list(request):
    aldeia_list = Aldeia.objects.all()
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Aldeia',
        'aldeia_list' : aldeia_list,
        'total_dados' : len(aldeia_list)
    }
    return render(request,'population/custom/aldeia/aldeia_list.html',context)



@login_required
def aldeia_input(request):
    if request.POST :
        form = Aldeia_form(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Registu Ho susesu !')
            return redirect('population:aldeia')
            
        else : 
            messages.error(request,'Dados Prenxe Lalos Ou eziste Ona')
            return redirect('population:aldeia')
    else :
        
        form = Aldeia_form()
        context = {
            'title': 'Registo Dados ',
            'form' : form,
            }
        return render(request, 'population/custom/aldeia/aldeia_input.html', context)



@login_required
def aldeia_edit(request,id):
    getdata = Aldeia.objects.get(id = id)
    if request.POST :
        form = Aldeia_form(request.POST,instance = getdata)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Update Ho susesu !')
            return redirect('population:aldeia')
        else : 
            messages.error(request,'Dados Update Falla')
            return redirect('population:aldeia')
    else :
        form = Aldeia_form(instance = getdata)
        context = {
            'title': 'Atualiza Dados',
            'form' : form,
            }
        return render(request, 'population/custom/aldeia/aldeia_input.html', context)


@login_required
def aldeia_delete(request,id):
    getdata = Aldeia.objects.filter(id = id).delete()
    messages.success(request,'Dados Apaga Ho susesu !')
    return redirect('population:aldeia')



















@login_required
def citizen_list(request):
    citizen_list = Citizen.objects.all()
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Cidadaun',
        'citizen_list' : citizen_list,
        'total_dados' : len(citizen_list)
    }
    return render(request, 'population/custom/citizen/citizen_list.html', context)



@login_required
def citizen_input(request):
    if request.POST :
        form = Citizen_form(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Registu Ho susesu !')
            return redirect('population:citizen')
        else : 
            messages.error(request,'Dados Prenxe Lalos Ou eziste Ona')
            return redirect('population:citizen')
    else :
        
        form = Citizen_form()


        context = {
            'title': 'Registo Dados ',
            'form' : form,
            }
        return render(request, 'population/custom/citizen/citizen_input.html', context)



@login_required
def citizen_edit(request,id):
    getdata = Citizen.objects.get(id = id)
    if request.POST :
        form = Citizen_form(request.POST,instance = getdata)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Update Ho susesu !')
            return redirect('population:citizen')
        else : 
            messages.error(request,'Dados Update Falla')
            return redirect('population:citizen')
    else :
        form = Citizen_form(instance = getdata)
        context = {
            'title': 'Atualiza Dados',
            'form' : form,
            }
        return render(request, 'population/custom/citizen/citizen_input.html', context)


@login_required
def citizen_delete(request,id):
    getdata = Citizen.objects.filter(id = id).delete()
    messages.success(request,'Dados Apaga Ho susesu !')
    return redirect('population:citizen')







@login_required
def religion_list(request):
    religion_list = Religion.objects.all()
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Relijiaun',
        'religion_list' : religion_list,
        'total_dados' : len(religion_list)
    }
    return render(request, 'population/custom/religion/religion_list.html', context)

    

@login_required
def religion_input(request):
    if request.POST :
        form = Religion_form(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Registu Ho susesu !')
            return redirect('population:religion')
        else : 
            messages.error(request,'Dados Prenxe Lalos Ou eziste Ona')
            return redirect('population:religion')
    else :
        
        form = Religion_form()
        context = {
            'title': 'Registo Dados ',
            'form' : form,
            }
        return render(request, 'population/custom/religion/religion_input.html', context)



@login_required
def religion_edit(request,id):
    getdata = Religion.objects.get(id = id)
    if request.POST :
        form = Religion_form(request.POST,instance = getdata)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Update Ho susesu !')
            return redirect('population:religion')
        else : 
            messages.error(request,'Dados Update Falla')
            return redirect('religion')
    else :
        form = Religion_form(instance = getdata)
        context = {
            'title': 'Atualiza Dados',
            'form' : form,
            }
        return render(request, 'population/custom/religion/religion_input.html', context)


@login_required
def religion_delete(request,id):
    getdata = Religion.objects.filter(id = id).delete()
    messages.success(request,'Dados Apaga Ho susesu !')
    return redirect('population:religion')




@login_required
def profession_list(request):
    profession_list = Profession.objects.all()
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Profisaun',
        'profession_list' : profession_list,
        'total_dados' : len(profession_list)
    }
    return render(request, 'population/custom/profession/profession_list.html', context)

    

@login_required
def profession_input(request):
    if request.POST :
        form = Profession_form(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Registu Ho susesu !')
            return redirect('population:profession')
        else : 
            messages.error(request,'Dados Prenxe Lalos Ou eziste Ona')
            return redirect('population:profession')
    else :
        
        form = Profession_form()
        context = {
            'title': 'Registo Dados ',
            'form' : form,
            }
        return render(request, 'population/custom/profession/profession_input.html', context)



@login_required
def profession_edit(request,id):
    getdata = Profession.objects.get(id = id)
    if request.POST :
        form = Profession_form(request.POST,instance = getdata)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Update Ho susesu !')
            return redirect('population:profession')
        else : 
            messages.error(request,'Dados Update Falla')
            return redirect('profession')
    else :
        form = Profession_form(instance = getdata)
        context = {
            'title': 'Atualiza Dados',
            'form' : form,
            }
        return render(request, 'population/custom/profession/profession_input.html', context)


@login_required
def profession_delete(request,id):
    getdata = Profession.objects.filter(id = id).delete()
    messages.success(request,'Dados Apaga Ho susesu !')
    return redirect('population:profession')







@login_required
def level_education_list(request):
    leve_education_list = Level_Education.objects.all()
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Habilitasaun literaria',
        'leve_education_list' : leve_education_list,
        'total_dados' : len(leve_education_list)
    }
    return render(request, 'population/custom/level_education/level_education_list.html', context)

    

@login_required
def level_education_input(request):
    if request.POST :
        form = Level_Education_form(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Registu Ho susesu !')
            return redirect('population:level_education')
        else : 
            messages.error(request,'Dados Prenxe Lalos Ou eziste Ona')
            return redirect('population:level_education')
    else :
        
        form = Level_Education_form()
        context = {
            'title': 'Registo Dados ',
            'form' : form,
            }
        return render(request, 'population/custom/level_education/level_education_input.html', context)



@login_required
def level_education_edit(request,id):
    getdata = Level_Education.objects.get(id = id)
    if request.POST :
        form = Level_Education_form(request.POST,instance = getdata)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Update Ho susesu !')
            return redirect('population:level_education')
        else : 
            messages.error(request,'Dados Update Falla')
            return redirect('population:level_education')
    else :
        form = Level_Education_form(instance = getdata)
        context = {
            'title': 'Atualiza Dados',
            'form' : form,
            }
        return render(request, 'population/custom/level_education/level_education_input.html', context)


@login_required
def level_education_delete(request,id):
    getdata = Level_Education.objects.filter(id = id).delete()
    messages.success(request,'Dados Apaga Ho susesu !')
    return redirect('population:level_education')







@login_required
def familyposition_list(request):
    familyposition_list = FamilyPosition.objects.all()
    context = {
        # 'totalmembru' : totalmembru,
        'title': 'Pozisaun Familia',
        'familyposition_list' : familyposition_list,
        'total_dados' : len(familyposition_list)
    }
    return render(request, 'population/custom/familyposition/familyposition_list.html', context)

    

@login_required
def familyposition_input(request):
    if request.POST :
        form = FamilyPosition_form(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Registu Ho susesu !')
            return redirect('population:familyposition')
        else : 
            messages.error(request,'Dados Prenxe Lalos Ou eziste Ona')
            return redirect('population:familyposition')
    else :
        
        form = FamilyPosition_form()
        context = {
            'title': 'Registo Dados ',
            'form' : form,
            }
        return render(request, 'population/custom/familyposition/familyposition_input.html', context)



@login_required
def familyposition_edit(request,id):
    getdata = FamilyPosition.objects.get(id = id)
    if request.POST :
        form = FamilyPosition_form(request.POST,instance = getdata)
        if form.is_valid() : 
            form.save()
            messages.success(request,'Dados Update Ho susesu !')
            return redirect('population:familyposition')
        else : 
            messages.error(request,'Dados Update Falla')
            return redirect('population:familyposition')
    else :
        form = FamilyPosition_form(instance = getdata)
        context = {
            'title': 'Atualiza Dados',
            'form' : form,
            }
        return render(request, 'population/custom/familyposition/familyposition_input.html', context)


@login_required
def familyposition_delete(request,id):
    getdata = FamilyPosition.objects.filter(id = id).delete()
    messages.success(request,'Dados Apaga Ho susesu !')
    return redirect('population:familyposition')