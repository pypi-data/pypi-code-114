from .models import Population,Family
from django.utils import timezone


def getlastid_kinos(table_name,id_suku):
    newid = 0
    result = table_name.objects.filter(village = id_suku).last()

    if result:
        getid = str(result.id)
        if len(id_suku) == 1 :
            cleanid_suku = getid[4 :]
        elif len(id_suku) == 2 :
            cleanid_suku = getid[5 :]
        elif len(id_suku) == 3 :
            cleanid_suku = getid[6 :]
        elif len(id_suku) == 4 :
            cleanid_suku = getid[7 :]            

        getlast = int(cleanid_suku) + 1
        newid = str(id_suku)+str("000")+str(getlast)
    else:
        newid = str(id_suku)+str("000")+"1"
    return newid

def getlastid_kinosrp(table_name,id_suku):

    newid = 0

    result = table_name.objects.filter(population__village = id_suku).last()
    if result:

        getid = str(result.id)
        print("koko : ")
        print(getid)
        print(id_suku)

        if len(id_suku) == 1 :
            cleanid_suku = getid[4 :]

        elif len(id_suku) == 2 :
            cleanid_suku = getid[5 :]
        elif len(id_suku) == 3 :
            cleanid_suku = getid[6 :]
        elif len(id_suku) == 4 :
            cleanid_suku = getid[7 :]

        getlast = int(cleanid_suku) + 1

        newid = str(id_suku)+str("000")+str(getlast)
    else:
        newid = str(id_suku)+str("000")+"1"
    return newid


def getlastid_kinosuser(table_name,id_suku):

    newid = 0

    result = table_name.objects.filter(employee__village = id_suku).last()
    if result:

        getid = str(result.id)


        if len(id_suku) == 1 :
            cleanid_suku = getid[4 :]

        elif len(id_suku) == 2 :
            cleanid_suku = getid[5 :]
        elif len(id_suku) == 3 :
            cleanid_suku = getid[6 :]
        elif len(id_suku) == 4 :
            cleanid_suku = getid[7 :]

        getlast = int(cleanid_suku) + 1

        newid = str(id_suku)+str("000")+str(getlast)
    else:
        newid = str(id_suku)+str("000")+"1"
    return newid

def getnewidp(id_suku):
    result = Population.objects.last()
    newid = 0 
    if result:
	    newid = result.id + 1
    else:
	    newid = 1
    id = str(id_suku)+str(newid) 
    return id

def createnewid(id_suku):
    newid = timezone.now().strftime("%y%m%d")
    id = str(id_suku)+str(newid)
    return id

def getnewidf():
    result = Family.objects.last()
    newid = 0 
    if result:
	    newid = result.id + 1
    else:
	    newid = 1
    id = newid
    return id

def getfulan():

    getfulan = [
        {"fulan" :"Janeiru","id" : "1"},
        {"fulan" : "Fevereiru","id" : "2"},
        {"fulan" : "Marsu","id" : "3"},
        {"fulan" : "Abril","id" : "4"},
        {"fulan" : "Maio","id" : "5"},
        {"fulan" : "Junhu","id" : "6"},
        {"fulan" : "Julhu","id" : "7"},
        {"fulan" : "Agostu","id" : "8"},
        {"fulan" : "Setembru","id" : "9"},
        {"fulan" : "Outubru","id" : "10"},
        {"fulan" : "Novembru","id" : "11"},
        {"fulan" : "Dezembru","id" : "12"},
        ]
    return getfulan