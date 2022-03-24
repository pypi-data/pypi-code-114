from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Level_Education,Temporary
from population.utils import getnewidp,getnewidf
from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,Death_form,Migration_form,Migrationout_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from population.utils import getfulan
from django.db.models import Count
from django.contrib import messages

import datetime
from django.db.models.functions import ExtractYear
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404
from employee.models import *
from django.db.models import Q
from datetime import datetime, timedelta

from calendar import monthrange
import datetime



@login_required
def reportb4(request):

    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)
    fulan = getfulan()
    tinan = DetailFamily.objects.values(year=ExtractYear('population__date_register')).filter(Q(status = True) & Q(population__village__id =  userAddress.employee.village.id)).annotate(total=Count('population__id')).order_by('year')
    cidadaun = Citizen.objects.all()
    edukasaun = Level_Education.objects.all()
    context = {
        'title': 'Populasaun Suku',
        'tinan' : tinan,
        'cidadaun' : cidadaun,
        'fulan' : fulan,
        'title' : 'Relatoriu Dadus Rekapitulasaun Populasaun',
    }
    return render(request, 'population/report/b4/report-b4.html',context)



@login_required
def reportb4_print(request):
    userAddress = get_object_or_404(EmployeeUser,user__id=request.user.id)



    year = request.GET['tinan']
    fulan = request.GET['fulan']
    loronikus = monthrange(int(year), int(fulan))
    start_date = "2000-01-01"
    end_date = year + "-" +fulan+ "-"+"1"
    end_date_last = year + "-" +fulan+ "-"+str(loronikus[1])


   




    aldeia = Aldeia.objects.filter(Q(village__id =  userAddress.employee.village.id))
    family_member = []

   


    for dadosaldeia in aldeia.iterator() :


        # Hahu Quantidade populasaun Inisiu Fulan Ida ne’e
        #Qtd.Xefe Familia p1
        p1qxefefamilia = DetailFamily.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(family_position = 1) & Q(population__status_datap = 'ac') & Q(population__date_register__range=(start_date, end_date)) &  Q(population__aldeia__id = dadosaldeia.id) & Q(status = True)).count()
        print("chefe familia")
        print(p1qxefefamilia)


        #populasaun Estrangeiru 4,5,6
        #Estranjeiru Mane
        p1estrangeiromane  = Migration.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(cidadaunm = 2) & Q(population__date_register__range=(start_date, end_date)) & Q(population__gender = 'm') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #Estranjeiru Feto
        p1estrangeirofeto  = Migration.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(cidadaunm = 2) & Q(population__date_register__range=(start_date, end_date)) & Q(population__gender = 'f') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p1estrangeiroseluk  = Migration.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(cidadaunm = 2) & Q(population__date_register__range=(start_date, end_date)) & Q(population__gender = 's') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()









        #populasaun tls Original
        p1tlsmane  = DetailFamily.objects.filter(Q(population__village__id =  userAddress.employee.village.id) & Q(population__gender = 'm') & Q(status = True) 
        & Q(population__date_register__range=(start_date, end_date)) & Q(population__status_datap = 'ac') & Q(population__type_data = 'f') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #populasaun suku laran  Feto
        p1tlsfeto  = DetailFamily.objects.filter(Q(population__gender = 'f') & Q(status = True) & Q(population__type_data = 'f') & Q(population__date_register__range=(start_date, end_date)) & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++ 
        p1tlsseluk  = DetailFamily.objects.filter(Q(population__gender = 's') & Q(status = True) & Q(population__type_data = 's') & Q(population__date_register__range=(start_date, end_date)) & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        

        #populasaun TLS suku migrasaun 
        p1tlsmane2  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__date_register__range=(start_date, end_date)) & Q(population__gender = 'm') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #populasaun suku laran tls Feto
        p1tlsfeto2  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__date_register__range=(start_date, end_date)) & Q(population__gender = 'f') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p1tlsseluk2  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__date_register__range=(start_date, end_date)) & Q(population__gender = 's') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()


        p1tlsmane = p1tlsmane + p1tlsmane2
        p1tlsfeto = p1tlsfeto + p1tlsfeto2
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p1tlsseluk = p1tlsseluk + p1tlsseluk2


   


        #Quantidade membro Familia
        p1qmembrufamilia = DetailFamily.objects.filter(Q(status = True) & Q(population__status_datap = 'ac') & Q(population__date_register__range=(start_date, end_date)) & Q(population__aldeia__id = dadosaldeia.id)).count()

        print("Membru Familia")
        print(p1qmembrufamilia)

        if p1qxefefamilia > p1qmembrufamilia :
            p1qmembrufamilia =   p1qxefefamilia - p1qmembrufamilia
        else : 
            p1qmembrufamilia =   p1qmembrufamilia - p1qxefefamilia




        #Quantidade Populasaun
        p1qpopulasaun = DetailFamily.objects.filter(Q(population__status_datap = 'ac') & Q(status = True) & Q(population__date_register__range=(start_date, end_date)) & Q(population__aldeia__id = dadosaldeia.id)).count()




        #Aumenta
        # p3emorisemane = Migration.objects.filter(Q(family_position = 1) & Q(population__status_datap='ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #aumenta moris

        #Populasaun Temporario Etrangeiro Ne'ebe moris iha suku
        p3morisemane  = Temporary.objects.filter(Q(cidadaunt = 2) & Q(population__gender = 'm')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan) & Q(population__type_data='mo')).count()
        #Populasaun Etrangeiro Ne'ebe moris sexu feto temporario
        p3morisefeto  = Temporary.objects.filter(Q(cidadaunt = 2) & Q(population__gender = 'f')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan) & Q(population__type_data='mo')).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3moriseseluk  = Temporary.objects.filter(Q(cidadaunt = 2) & Q(population__gender = 's')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan) & Q(population__type_data='mo')).count()



       #Populasaun Temporario timor oan ne'ebe moris
        p3morisemanetemp  = Temporary.objects.filter(Q(cidadaunt = 1) & Q(population__gender = 'm')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan) & Q(population__type_data='mo')).count()
        #Populasaun timor Ne'ebe moris sexu feto temporario
        p3morisefetotemp  = Temporary.objects.filter(Q(cidadaunt = 1) & Q(population__gender = 'f')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan) & Q(population__type_data='mo')).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3moriseseluktemp  = Temporary.objects.filter(Q(cidadaunt = 1) & Q(population__gender = 's')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan) & Q(population__type_data='mo')).count()



        #Populasaun timor oan ne'ebe muda no  moris sexu mane
        p3moristmane  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__gender = 'm')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan)).count()
        #Populasaun timor oan ne'ebe muda no  moris sexu feto
        p3moristfeto  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__gender = 'f')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++        
        p3moristseluk  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__gender = 's')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan)).count()
         #Populasaun timor oan ne'ebe iha suku laran no  moris sexu mane
        

        p3moristmane2  = DetailFamily.objects.filter(Q(population__nationality = '1')  & Q(population__gender = 'm')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan)).count()
        #Populasaun timor oan ne'ebe iha suku laran no  moris sexu feto
        p3moristfeto2  = DetailFamily.objects.filter(Q(population__nationality = '1')  & Q(population__gender = 'f')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3moristseluk2  = DetailFamily.objects.filter(Q(population__nationality = '1')  & Q(population__gender = 's')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan)).count()



        p3moristmane2 = p3moristmane + p3moristmane2 + p3morisemanetemp
        p3moristfeto2 = p3moristfeto + p3moristfeto2 + p3morisefetotemp
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3moristseluk2 = p3moristseluk + p3moristseluk2 + p3moriseseluktemp










        #muda 
        #muda tama estrangeiro
        p3mudatamaemane  = Migration.objects.filter(Q(cidadaunm = 2) & Q(population__gender = 'm')  & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
        p3mudatamaefeto  = Migration.objects.filter(Q(cidadaunm = 2) & Q(population__gender = 'f')  & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3mudatamaeseluk  = Migration.objects.filter(Q(cidadaunm = 2) & Q(population__gender = 's')  & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
       
    
        p3mudatamatmane  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__gender = 'm')  & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
        p3mudatamatfeto  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__gender = 'f')  & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3mudatamatseluk  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__gender = 's')  & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
       




        #menus mate
        # estrangeiro 
        
        p3mateemane  = Death.objects.filter(Q(population__nationality = '2') & Q(population__gender = 'm') & Q(population__status_datap = 'ma')  &  Q(population__aldeia__id = dadosaldeia.id) & Q(date__year = year) & Q(date__month = fulan)).count()
        p3mateefeto  = Death.objects.filter(Q(population__nationality = '2') & Q(population__gender = 'f') & Q(population__status_datap = 'ma')  &  Q(population__aldeia__id = dadosaldeia.id) & Q(date__year = year) & Q(date__month = fulan)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3mateeseluk  = Death.objects.filter(Q(population__nationality = '2') & Q(population__gender = 's') & Q(population__status_datap = 'ma')  &  Q(population__aldeia__id = dadosaldeia.id) & Q(date__year = year) & Q(date__month = fulan)).count()
          
       
       # timor 
        p3matetmane  = Death.objects.filter(Q(population__nationality = '1') & Q(population__gender = 'm') & Q(population__status_datap = 'ma')  &  Q(population__aldeia__id = dadosaldeia.id) & Q(date__year = year) & Q(date__month = fulan)).count()
        p3matetfeto  = Death.objects.filter(Q(population__nationality = '1') & Q(population__gender = 'f') & Q(population__status_datap = 'ma')  &  Q(population__aldeia__id = dadosaldeia.id) & Q(date__year = year) & Q(date__month = fulan)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3matetseluk  = Death.objects.filter(Q(population__nationality = '1') & Q(population__gender = 's') & Q(population__status_datap = 'ma')  &  Q(population__aldeia__id = dadosaldeia.id) & Q(date__year = year) & Q(date__month = fulan)).count()




        #menus muda sai
        #estrageiro

        p3mudasaiemane  = Migrationout.objects.filter(Q(population__nationality = '2') & Q(population__gender = 'm') & Q(population__status_datap = 'mu')   & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
        p3mudasaiefeto  = Migrationout.objects.filter(Q(population__nationality = '2') & Q(population__gender = 'f') & Q(population__status_datap = 'mu')   & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3mudasaieseluk  = Migrationout.objects.filter(Q(population__nationality = '2') & Q(population__gender = 's') & Q(population__status_datap = 'mu')   & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()


        p3mudasaitmane  = Migrationout.objects.filter(Q(population__nationality = '1') & Q(population__gender = 'm') & Q(population__status_datap = 'mu')   & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
        p3mudasaitfeto  = Migrationout.objects.filter(Q(population__nationality = '1') & Q(population__gender = 'f') & Q(population__status_datap = 'mu')   & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        p3mudasaitseluk  = Migrationout.objects.filter(Q(population__nationality = '1') & Q(population__gender = 's') & Q(population__status_datap = 'mu')   & Q(population__aldeia__id = dadosaldeia.id) & Q(date_migration__year = year) & Q(date_migration__month = fulan)).count()
          






        dataagora = end_date_last





    # Total Populasaun Fim do Mes



        # p3morisemane  = Temporary.objects.filter(Q(cidadaunt = 2) & Q(population__gender = 'm')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan) & Q(population__type_data='te')).count()


        # #Populasaun Etrangeiro Ne'ebe moris sexu feto temporario
        # p3morisefeto  = Temporary.objects.filter(Q(cidadaunt = 2) & Q(population__gender = 'f')  & Q(population__aldeia__id = dadosaldeia.id) & Q(population__date_of_bird__year = year) & Q(population__date_of_bird__month = fulan) & Q(population__type_data='te')).count()




        #Estranjeiru Mane
        fimestrangeiromane  = Migration.objects.filter(Q(cidadaunm = 2) & Q(population__date_register__range=(start_date, dataagora)) & Q(population__gender = 'm') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #Estranjeiru Feto
        fimestrangeirofeto  = Migration.objects.filter(Q(cidadaunm = 2) & Q(population__date_register__range=(start_date, dataagora)) & Q(population__gender = 'f') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        fimestrangeiroseluk  = Migration.objects.filter(Q(cidadaunm = 2) & Q(population__date_register__range=(start_date, dataagora)) & Q(population__gender = 's') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
       
        # fimestrangeiromane  = Temporary.objects.filter(Q(cidadaunt = 2) & Q(date_arive__range=(start_date, dataagora)) & Q(population__gender = 'm') & Q(population__status_datap = 'te') & Q(population__aldeia__id = dadosaldeia.id)).count()

    
        # fimestrangeirofeto  = Temporary.objects.filter(Q(cidadaunt = 2) & Q(date_arive__range=(start_date, dataagora)) & Q(population__gender = 'f') & Q(population__status_datap = 'te') & Q(population__aldeia__id = dadosaldeia.id)).count()





        #populasaun suku laran Mane 
        fimp1tlsmane  = DetailFamily.objects.filter(Q(population__gender = 'm') & Q(population__date_register__range=(start_date, dataagora))  & Q(status= True) & Q(population__status_datap = 'ac') & Q(population__type_data = 'f') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #populasaun suku laran  Feto
        fimp1tlsfeto  = DetailFamily.objects.filter(Q(population__gender = 'f') & Q(population__type_data = 'f') & Q(population__date_register__range=(start_date, dataagora))  & Q(status = True) & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        fimp1tlsseluk  = DetailFamily.objects.filter(Q(population__gender = 's') & Q(population__type_data = 'f') & Q(population__date_register__range=(start_date, dataagora))  & Q(status = True) & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
      


        #populasaun suku migrasaun tls  mane
        fimp1tlsmane2  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__date_register__range=(start_date, dataagora)) & Q(population__gender = 'm') & Q(population__id_family='i') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #populasaun suku laran tls Feto
        fimp1tlsfeto2  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__date_register__range=(start_date, dataagora)) & Q(population__gender = 'f')  & Q(population__id_family='i') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        fimp1tlsseluk2  = Migration.objects.filter(Q(cidadaunm = 1) & Q(population__date_register__range=(start_date, dataagora)) & Q(population__gender = 's')  & Q(population__id_family='i') & Q(population__status_datap = 'ac') & Q(population__aldeia__id = dadosaldeia.id)).count()
       

        fimp1tlsmane = fimp1tlsmane + fimp1tlsmane2
        fimp1tlsfeto = fimp1tlsfeto + fimp1tlsfeto2
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        fimp1tlsseluk = fimp1tlsseluk + fimp1tlsseluk2


        #Qtd.Xefe Familia
        fimp1qxefefamilia = DetailFamily.objects.filter(Q(family_position = 1) & Q(population__status_datap = 'ac') & Q(population__date_register__range=(start_date, dataagora)) &  Q(population__aldeia__id = dadosaldeia.id)).count()
        

      #Quantidade membro Familia
        fimp1qmembrufamilia = DetailFamily.objects.filter(Q(status = True) 
        & Q(population__status_datap = 'ac') & Q(population__date_register__range=(start_date, dataagora)) & Q(population__aldeia__id = dadosaldeia.id)).count()
        fimp1qmembrufamilia = fimp1qmembrufamilia - fimp1qxefefamilia

        #Quantidade Populasaun
        fimp1qpopulasaun = DetailFamily.objects.filter(Q(status = True) 
        & Q(population__status_datap = 'ac') & Q(population__date_register__range=(start_date, dataagora)) & Q(population__aldeia__id = dadosaldeia.id)).count()






        family_member.append({
            'aldeia' : dadosaldeia.name,
            'p1qxefefamilia' : p1qxefefamilia,


            #Populasaun Estrangeiru
            'p1estrangeiromane' : p1estrangeiromane,
            'p1estrangeirofeto' : p1estrangeirofeto,
            'p1estrangeiroseluk' : p1estrangeiroseluk,

            #populasaun Suku
            'p1tlsmane' : p1tlsmane,
            'p1tlsfeto' : p1tlsfeto,
            'p1tlsseluk' : p1tlsseluk,


            'p1qmembrufamilia' : p1qmembrufamilia,
            'p1qpopulasaun' : p1qpopulasaun,

            #aumenta
            #Aumenta Moris
            #aumenta moris estrangiro mane,feto
            'p3morisemane' : p3morisemane,
            'p3morisefeto' : p3morisefeto,
            'p3moriseseluk' : p3moriseseluk,

            
            #aumenta moris Timor oan mane,feto
            'p3moristmane2' : p3moristmane2,
            'p3moristfeto2' : p3moristfeto2,
            'p3moristseluk2' : p3moristseluk2,
            



            #aumenta muda tama
            #muda tama estrageiro
            'p3mudatamaemane' : p3mudatamaemane,
            'p3mudatamaefeto' : p3mudatamaefeto,
            'p3mudatamaeseluk' : p3mudatamaeseluk,


            'p3mudatamatfeto' : p3mudatamatfeto,
            'p3mudatamatmane' : p3mudatamatmane,
            'p3mudatamatseluk' : p3mudatamatseluk,

            #menus 
            #menus mate 
            'p3mateemane' : p3mateemane,
            'p3mateefeto' : p3mateefeto,
            'p3mateeseluk' : p3mateeseluk,

            'p3matetmane' : p3matetmane,
            'p3matetfeto' : p3matetfeto,
            'p3matetseluk' : p3matetseluk,

            #menus muda sai
            'p3mudasaiefeto' : p3mudasaiefeto,
            'p3mudasaiemane' : p3mudasaiemane,
            'p3mudasaieseluk' : p3mudasaieseluk,

            'p3mudasaitfeto' : p3mudasaitfeto,
            'p3mudasaitmane' : p3mudasaitmane,
            'p3mudasaitseluk' : p3mudasaieseluk,


            #fim do mes
            #estrangeiro

            'fimestrangeiromane' : fimestrangeiromane,
            'fimestrangeirofeto' : fimestrangeirofeto,
            'fimestrangeiroseluk' : fimestrangeirofeto,

            'fimp1tlsmane' : fimp1tlsmane,
            'fimp1tlsfeto' : fimp1tlsfeto,
            'fimp1tlsseluk' : fimp1tlsseluk,

            'fimp1qxefefamilia' : fimp1qxefefamilia,
            'fimp1qmembrufamilia' : fimp1qmembrufamilia,
            'fimp1qpopulasaun' : fimp1qpopulasaun,







            })
        
        


 
    
    template = "population/report/b4/report-b4-print.html"
    context = {
        'title' : 'Relatorio Dados Rekapitulasaun Populasaun',
        'family_member' : family_member,
        'year' : year,
        'fulan' : fulan,
		'munisipiu' : userAddress.employee.village.administrativepost.municipality.name,
		'postu' : userAddress.employee.village.administrativepost.name,
		'suku' : userAddress.employee.village.name,

    } 

    return render(request,template, context)