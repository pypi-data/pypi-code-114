from django.db import models

import hashlib
from hashlib import sha512

from django.db import models
from django.contrib.auth.models import User
from django.core import validators




from custom.models import Municipality,AdministrativePost,Village,Aldeia


#note : Naran Tabela / aldeia = village , Suku = sucos

#note : Naran Tabela / aldeia = village , Suku = sucos

MARITAL_STATUS = (
        ("s", "Klosan"),
        ("c", "Kaben Nain"),
        ("d", "Fahe Malu"),
        ("f", "Faluk"),
    )


STATUS_DATA = (

        ("ma", "mate"),
        ("mu", "muda"),
        ("ac", "activu"),
    
    )


VURNERAVEL = (
        (True, "Lae"),
        (False, "Sim"),
    )

GENDER = (
        ("m", "Mane"),
        ("f", "Feto"),
        ("s", "Seluk"),
    )

TYPE_LANGUAGE = (
        ("o", "Origen"),
        ("i", "International"),

    )


KATEGORY_TRANSFERENCE = (
        ("o", "out"),
        ("i", "in"),
    )


READ_ALPHABET = (
        ("s", "Sim"),
        ("l", "Lae"),
    )





CITIZEN_VILLAGE = (
        ("a", "Adkeridu"),
        ("o", "Original"),

    )



TYPE_DATA = (
        ("p", "Population"),
        ("f", "Family"),
        # ("d", "death"),
        ("m", "migration"),
        ("te", "Populasaun Temporariu"),
        ("mo", "Bebe Moris"),
        ("test", "Test"),
    )


class Language(models.Model):
    name = models.CharField(max_length = 50,verbose_name='Naran Lingua')
    type_language = models.CharField(max_length = 1,verbose_name='Tipu Lingua',choices=TYPE_LANGUAGE,null=True,blank=True)
    hashed = models.CharField(max_length=32,null=True,blank=True)
    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    class Meta:
        verbose_name_plural='Dadus Custom Ba Lingua'


class Religion(models.Model):
    name = models.CharField(max_length = 50,verbose_name='Relijiun')
    hashed = models.CharField(max_length=32,null=True,blank=True)
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    class Meta:
        verbose_name_plural='Dadus Custom Ba Relijiaun'

class Profession(models.Model):
    name = models.CharField(max_length = 50 ,verbose_name='Profisaun Servisu')
    hashed = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    class Meta:
        verbose_name_plural='Dadus Custom Ba Profisaun'

    # def save(self, *args, **kwargs):
	#     self.hashed = hashliba.md5(str(self.id).encode()).hexdigest()
	#     return super(Profession, self).save(*args, **kwargs)


class FamilyPosition(models.Model):
    name = models.CharField(max_length = 50 ,verbose_name='Pozisaun iha Família')
    hashed = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    class Meta:
        verbose_name_plural='Dadus Custom Ba Pozisaun Família'


class Citizen(models.Model):
    name = models.CharField(max_length = 20 ,verbose_name='Cidadania Nasaun')
    hashed = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    class Meta:
        verbose_name_plural='Dadus Custom Ba Sidadaun'

class Level_Education(models.Model):
    name = models.CharField(max_length = 50 ,verbose_name='Habilitasaun Literariu')
    hashed = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        template = '{0.name}'
        return template.format(self)


# atbela population utiliza hodi registu dados populasaun husi aldeia iha suku laran ou mos husi suku  seluk. 
    class Meta:
        verbose_name_plural='Dadus Custom Ba Level Edukasaun'


class Deficient(models.Model):
    name = models.CharField(max_length=100,verbose_name="Kondisaun Fiziku")
    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    class Meta:
        verbose_name_plural = 'Dadus Custom Ba Difisiente'

# id ,village,aldeia,profession,citizenp,religion,user_created,unique_id,name,date_of_bird,place_of_bird,gender,marital_status,level_education,readalatin,readaarabe,readachina,nu_bi,id_pasaporte,id_family,descriptionp,imagen,status_datap,type_data,date_created,hashed
class Population(models.Model):
    id = models.BigIntegerField(primary_key=True)
    village = models.ForeignKey(Village,on_delete=models.CASCADE,verbose_name='Suku') 
    # field village sei prenxe id_suku  husi suku ne'ebe registu dados 
    aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,verbose_name='Hela Fatin / Aldeia ',null=True,blank=True) # Aldeia ba cidadaun nian
    administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null = True, blank =  True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null = True, blank =  True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE,verbose_name='Profisaun',null=True,blank=True)
    citizenp =  models.CharField(max_length=15,choices=CITIZEN_VILLAGE,verbose_name='Sidadania',null=True,blank=True)  
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE,verbose_name='Relijiaun',null=True,blank=True)
    date_register = models.DateField(verbose_name='Data Rejistu',null=True,blank=True)
    unique_id = models.CharField(max_length=50,null=True,blank=True,verbose_name='Id Uniku / Uza Ba test Husik Mamuk Deit')
    name = models.CharField(max_length=100,verbose_name="Naran Kompletu/Alias")
    date_of_bird = models.DateField(verbose_name='Data Moris')
    place_of_bird = models.CharField(max_length=100,verbose_name='Fatin Moris')

    gender = models.CharField(max_length=4,choices=GENDER,verbose_name='Seksu')
    marital_status = models.CharField(max_length=15,choices=MARITAL_STATUS,verbose_name='Estadu Civil',null=True,blank=True)  
    level_education = models.ForeignKey(Level_Education, on_delete=models.CASCADE,verbose_name='Habilitasaun Literaria ikus liu',blank=True,null=True)
    language = models.CharField(max_length=50,blank=True,null=True)
    readalatin = models.CharField(max_length=15,choices=READ_ALPHABET,verbose_name='Hatene Le Alfabetu Latin ?',blank=True,null=True)
    readaarabe = models.CharField(max_length=15,choices=READ_ALPHABET,verbose_name='Hatene Le Alfabetu Arabe ?',blank=True,null=True)
    readachina = models.CharField(max_length=15,choices=READ_ALPHABET,verbose_name='Hatene Le Alfabetu China ?',blank=True,null=True)    
    nu_bi = models.CharField(max_length=25,verbose_name="Nú. Kartaun Identidade (BI)",blank=True,null=True)
    phone = models.CharField(max_length=25,verbose_name="Nú. Telefone",blank=True,null=True)
    nu_e = models.CharField(max_length=25,verbose_name="Nú. Kartaun Eleitoral",blank=True,null=True)
    nu_p = models.CharField(max_length=50,verbose_name="Nú. Pasaporte",blank=True,null=True)
    id_family = models.CharField(max_length=20,verbose_name='Nú. Kartaun  Fixa Família',blank=True,null=True)
    nationality = models.CharField(max_length=1, blank=True,null=True)
    descriptionp = models.TextField(verbose_name='Obs', blank=True,null=True)
    imagen = models.ImageField(upload_to = 'img/population/', blank=True,null=True,verbose_name='Imaen / Uza Ba test Husik Mamuk Deit',default='img/population/imagenlaiha.png') 
    status_datap = models.CharField(max_length=2,choices=STATUS_DATA,blank=True,null=True)
    deficient =  models.ForeignKey(Deficient,on_delete=models.CASCADE,verbose_name='Kondisaun')
    vulnerable =  models.BooleanField(choices=VURNERAVEL,default=False,blank=True,null=True,verbose_name="Pesoa Vulnerável ...?")
    # field status_datap  karik ema ne'e mate ona nia status_datap data sei muda ba false
    type_data = models.CharField(max_length=15,choices=TYPE_DATA,verbose_name='Tipu Dados') 
    # type_data utiliza hodi halo diferenca dados populasaun nee  registu husi fungsionamento ida ne'ebe ex fixa famlia ka populasaun trasnferencia
    date_created = models.DateField()
    user_created =  models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    hashed = models.CharField(max_length=40,null=True,blank=True)


    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    class Meta:
        verbose_name_plural = 'Livru Rejistu Populasaun'

# Fixa Familia Utiliza hodi registu dadso familia uma kain no membru familia uma kain.
# dados membru familia foti husi tabela population


class Family(models.Model):
    id = models.BigIntegerField(primary_key=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE,null = True, blank =  True)
    administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null = True, blank =  True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null = True, blank =  True)
    aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,null = True, blank =  True)
    user_created =  models.ForeignKey(User, on_delete=models.CASCADE)
    id_family = models.BigIntegerField(verbose_name='Nú. Kartaun  Fixa FamÍlia', null = True, blank =  True)
    
    data_registu = models.DateField(verbose_name='Data Rejistu',null=True,blank=True) 
    fdescription = models.TextField(verbose_name='Observasaun')
    date_created = models.DateField()
    hashed = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        template = '{0.id_family}'
        return template.format(self)
    class Meta:
        verbose_name_plural = 'Dadus Custom Ba FamÍlia'


class DetailFamily(models.Model):
    id = models.BigIntegerField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    population = models.ForeignKey(Population, on_delete=models.CASCADE,verbose_name='Hili Populasaun Iha Suku')
    user_created =  models.ForeignKey(User, on_delete=models.CASCADE)
    family_position = models.ForeignKey(FamilyPosition, on_delete=models.CASCADE, verbose_name='Pozisaun iha FamÍlia')
    # family_position = models.CharField(max_length=4,choices=FAMILY_POSITION)
    status = models.BooleanField(default=True,verbose_name='Ativu') 
    # Field status_datadp :  sei  sai false karik membru familia ne'e iha laran hari fali tan familia foun.
    date_created = models.DateField()
    hashed = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        template = '{0.family_position}'
        return template.format(self)

    class Meta:
        verbose_name_plural = 'Dadus Detail FamÍlia'


class FamilyCardOnline(models.Model):
    village = models.ForeignKey(Village,on_delete=models.CASCADE,  verbose_name='Suku') 
    administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null = True, blank =  True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null = True, blank =  True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    cordinate = models.TextField(default=True,verbose_name='Ativu') 
    status = models.BooleanField(default=True,verbose_name='Ativu') 
    date_created = models.DateField()
    user_created = models.CharField(max_length=12,null=True,blank=True)
    hashed = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        template = '{0.cordinate}'
        return template.format(self)

    def __str__(self):
        template = '{0.cordinate}'
        return template.format(self)
    class Meta:
        verbose_name_plural = 'Dadus Kartaun Família Online'

class Temporary(models.Model):
    id = models.BigIntegerField(primary_key=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE) # id suku husi suku ne'ebe registu dados
    population = models.ForeignKey(Population, on_delete=models.CASCADE , verbose_name='Identidade Populasaun')
    user_created =  models.ForeignKey(User, on_delete=models.CASCADE)
    from_place =  models.CharField(verbose_name="Mai Husi",null=True,blank=True,max_length=50)
    cidadaunt = models.ForeignKey(Citizen,on_delete=models.CASCADE,verbose_name='Cidadania',null=True,blank=True)   
    purpose = models.TextField(verbose_name='Intensaun Mai',null=True,blank=True)
    residence = models.TextField(verbose_name='Naran no hela fatin Visitor',null=True,blank=True) # ema ne'ebe simu bainaka refere
    date_arive = models.DateField(verbose_name='Data Mai',null=True,blank=True)
    date_return = models.DateField(verbose_name='Data Fila',null=True,blank=True)
    descriptionte = models.TextField(verbose_name='Observasaun',null=True,blank=True)
    date_created = models.DateField()
    hashed = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        template = '{0.purpose}'
        return template.format(self)
    class Meta:
        verbose_name_plural = 'Dadus Populasaun Temporáriu'

#id,village,population,user_created,cidadaunm,from_aldeia,from_nation,date_migration,descriptionm,date_created,hashed


class Migrationout(models.Model):
    id = models.BigIntegerField(primary_key=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE) # id suku husi suku ne'ebe registu dados
    population = models.ForeignKey(Population, on_delete=models.CASCADE)
    user_created =  models.ForeignKey(User, on_delete=models.CASCADE)
    cidadaunmo = models.ForeignKey(Citizen,on_delete=models.CASCADE,verbose_name="Muda Ba Ne'ebe ..? ",null=True,blank=True) 
    to_aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,verbose_name="Muda ba Aldeia ne'ebe",null=True,blank=True)
    to_nation = models.CharField(max_length=100,verbose_name="Muda Ba Nasaun Ne'ebe",null=True,blank=True)
    date_migration = models.DateField(verbose_name='Data Muda Sai',null=True,blank=True)
    descriptionmo = models.TextField(verbose_name='Observasaun',null=True,blank=True)
    date_created = models.DateField()
    hashed = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        template = '{0.descriptionmo}'
        return template.format(self)

    class Meta:
        verbose_name_plural = 'Dadus Populasaun Mudansa'


class ChangeFamily(models.Model):
    id = models.BigIntegerField(primary_key=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE) # id suku husi suku ne'ebe registu dados
    familymember = models.ForeignKey(DetailFamily,on_delete=models.CASCADE)
    user_created =  models.ForeignKey(User, on_delete=models.CASCADE)
    date_change = models.DateField(verbose_name='Data Sai Husi Família',null=True,blank=True)
    descriptioncf = models.TextField(verbose_name='Observasaun',null=True,blank=True)
    date_created = models.DateField()
    hashed = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        template = '{0.descriptioncf}'
        return template.format(self)
    class Meta:
        verbose_name_plural = 'Dadus Mudansa Família'

    
class Migration(models.Model):
    id = models.BigIntegerField(primary_key=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null = True, blank =  True,verbose_name="Mai husi Suku ne'ebe") # id suku husi suku ne'ebe registu dados
    administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null = True, blank =  True, verbose_name="Mai husi Postu Administrativu ne'ebe")
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null = True, blank =  True,verbose_name="Mai husi Munisípiu/Rejiaun ne'ebe")
    population = models.ForeignKey(Population, on_delete=models.CASCADE)
    user_created =  models.ForeignKey(User, on_delete=models.CASCADE)
    # field Kategory_transference atu halo diferenca dados iha tabela   ba populasaun aumenta ka menus
    cidadaunm = models.ForeignKey(Citizen,on_delete=models.CASCADE,verbose_name='Nasionalidade',null=True,blank=True) 
    from_aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,verbose_name="Mai husi aldeia ne'ebe",null=True,blank=True)

    migration_accept = models.BooleanField(default=False)
    user_accept =  models.CharField(max_length=5, null = True, blank = True)
    from_nation = models.CharField(max_length=100,verbose_name="Nasionalidade",null=True,blank=True)
    date_migration = models.DateField(null=True,blank=True,verbose_name='Data Muda mai iha suku')
    descriptionm = models.TextField(verbose_name='Observasaun',null=True,blank=True)
    date_created = models.DateField()
    hashed = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        template = '{0.descriptionm}'
        return template.format(self)

    class Meta:
        verbose_name_plural = 'Dadus Migrasaun Populasaun'

class Death(models.Model):
    id = models.BigIntegerField(primary_key=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE) # id suku husi
    population = models.ForeignKey(Population, on_delete=models.CASCADE)
    user_created =  models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Data')
    descriptiond = models.TextField(verbose_name='Observasaun',null=True)
    date_created = models.DateField()
    hashed = models.CharField(max_length=40,null=True,blank=True)

    def __str__(self):
        template = '{0.descriptiond}'
        return template.format(self)

    class Meta:
        verbose_name_plural = 'Dadus Populsaun Mate'
