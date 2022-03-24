from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from population.serializers import *

from django.conf import settings
from django.contrib.auth.hashers import make_password

# utiliza hodi extract data 
from django.utils.dateparse import parse_date


from django.utils import timezone
from population.models import FamilyCardOnline,Family,Population,DetailFamily

#utiliza ba redirect url direita husi class
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from django.contrib import messages

#utiliza ba chek login ou lae
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse


from django.db.models import Q
from employee.models import *



class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer
    def create(self, request):
        user = authenticate(username= request.data.get('username'), password = request.data.get('password'))


        if user is None:
            return Response({'message': 'No user found','status':False, 'data' : {}})
        else:

            if user.last_name == 'familycard20521693' : 
                return Response({'mensagen': 'susesu','id_familia': user.username, 'xave':user.first_name,})

            else : 
                return Response({'message': 'No user found','status':False, 'data' : {}})



class PerfilViewSet(viewsets.ViewSet):
    def list(self, request):

        key = request.GET['id']
        koa = key.split("F")
        lista_familia = []
        lista_xefefamilia = []

        idfamilia = int(koa[1])
        idsuku = int(koa[0])

        dadosfam = DetailFamily.objects.filter(Q(family__id_family = idfamilia ) & Q(family__village_id = idsuku) & Q(status = True))

        for dados in dadosfam.iterator():

            if dados.family_position.id == 1 :

                lista_xefefamilia.append({

                    'naran' : dados.population.name,
                    'id' : dados.population.id,
                    'sexu' : dados.population.gender,
                    'data_moris' : dados.population.date_of_bird,
                    'fatin_moris' : dados.population.place_of_bird,
                    'pozisun' : dados.family_position.name,
                    'nu_bi' : dados.population.nu_bi,
                    'imagen' : dados.population.imagen.url,
                    'localizasaun' : dados.population.village.administrativepost.municipality.name +"/"+dados.population.village.administrativepost.name +"/"+ dados.population.village.name+"/"+ dados.population.aldeia.name,
                })

            else :
               
                if dados.population.nu_bi == '' :
                    nubi = "Laiha"
                else : 
                    nu_bi = dados.population.nu_bi
                lista_familia.append({
                    'naran' : dados.population.name,
                    'id' :dados.population.id,
                    'sexu' : dados.population.gender,
                    'data_moris' : dados.population.date_of_bird,
                    'fatin_moris' : dados.population.place_of_bird,
                    'pozisun' : dados.family_position.name,
                    'nu_bi' : nu_bi,
                })



        # print(idfamilia)
        # print(idsuku)




        # co = request.GET['id']
        # categories = tbRequest.objects.filter(user_phone=co).order_by('-datetime')
        # koko = DadosRequestSerializer(categories, many=True)
        # return Response({ 'data': koko.data})
        return Response({ 
            'membru': lista_familia,
            'xefe': lista_xefefamilia,
            })


class AdressViewSet(viewsets.ViewSet):
    def list(self, request):

        key = request.GET['id']
        koa = key.split("F")
        lista_familia = []
        lista_xefefamilia = []

        idfamilia = int(koa[1])
        idsuku = int(koa[0])
        
        
        xefe = " Mariano Da Silva"
        dadosfam = FamilyCardOnline.objects.filter(Q(family__id_family = idfamilia ) & Q(family__village_id = idsuku) & Q(status = True))
        try:
            userAddress = Employee.objects.filter(Q(village__id = idsuku) & Q(is_end = False))[0]
            xefe = userAddress.first_name + " " + userAddress.last_name
        except :
            print("Xefe suku la iha")


   
        for dados in dadosfam.iterator() :
            korkoa = dados.cordinate.split(",")
            lista_xefefamilia.append({
                'lat' : korkoa[0],
                'lon' :  korkoa[1],
                'munisipiu' : dados.family.municipality.name,
                'postu' : dados.family.administrativepost.name,
                'suku' :  dados.family.village.name,
                'aldeia' : dados.family.aldeia.name,
                'xefe_suku' : xefe,
            })

        # co = request.GET['id']
        # categories = tbRequest.objects.filter(user_phone=co).order_by('-datetime')
        # koko = DadosRequestSerializer(categories, many=True)
        # return Response({ 'data': koko.data})
        return Response({ 
            'address': lista_xefefamilia,
            })