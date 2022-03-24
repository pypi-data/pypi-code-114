from django.urls import path,include
from population import views
from rest_framework.routers import DefaultRouter


app_name = 'population'


router = DefaultRouter()
router.register('login',views.LoginViewSet, basename='login')
router.register('perfil',views.PerfilViewSet, basename='perfil')
router.register('address',views.AdressViewSet, basename='address')




urlpatterns = [
   
   path('familyAPI/', include(router.urls)),

   path('',views.dashboard_population, name='dashboard_population'),



# Registu Populasaun
   path('reg_population/',views.family_list, name='reg_population'),
   path('family_input/',views.family_input, name='family_input'),
   path('detailfamily_list/<hashed>/',views.detailfamily_list, name='detailfamily_list'),
   path('family_edit/<hashed>/',views.family_edit, name='family_edit'),
   path('family_delete/<hashed>/',views.family_delete, name='family_delete'),


   
   path('familymember_input/<hashed>',views.familymember_input, name='familymember_input'),
   path('familymember_update/<hashed>',views.familymember_update, name='familymember_update'),
   path('familymember_updateep/<hashed>',views.familymember_updateep, name='familymember_updateep'),




#populasau muda suku
   path('familymember_out/<hashed>',views.familymember_out, name='familymember_out'),
   path('familymember_out_apaga/<hashed>',views.familymember_out_apaga, name='familymember_out_apaga'),

#populasaun mate
   path('familymember_mate/<hashed>',views.familymember_mate, name='familymember_mate'),
   path('familymember_mate_apaga/<hashed>',views.familymember_mate_apaga, name='familymember_mate_apaga'),
   path('familymember_delete/<hashed>',views.familymember_delete, name='familymember_delete'),


   path('familymember_desativu/<hashed>',views.familymember_desativu, name='familymember_desativu'),
   path('familymember_ativu/<hashed>',views.familymember_ativu, name='familymember_ativu'),

   path('familymember_change/<hashed>',views.familymember_change, name='familymember_change'),

#relatorio
   path('reportb1',views.reportb1, name='reportb1'),   
   path('reportb1_print',views.reportb1_print, name='reportb1_print'),

   path('reportb2',views.reportb2, name='reportb2'),  
   path('reportb2_print',views.reportb2_print,name='reportb2_print'),


   path('reportb3',views.reportb3, name='reportb3'),  
   path('reportb3_print',views.reportb3_print,name='reportb3_print'),



   path('reportb4',views.reportb4, name='reportb4'),  
   path('reportb4_print',views.reportb4_print,name='reportb4_print'),


   path('reportb5',views.reportb5, name='reportb5'),  
   path('reportb5_print/<hashed>',views.reportb5_print,name='reportb5_print'),



#relatorio Jeral grafiku 
   path('reportb1jeralMunicipality',views.reportb1jeralMunicipality, name='reportb1jeralMunicipality'),  
   path('reportb1jeralPostadministrative/<id>',views.reportb1jeralPostadministrative, name='reportb1jeralPostadministrative'),
   path('reportb1jeralVillage/<id>',views.reportb1jeralVillage, name='reportb1jeralVillage'),
   path('reportb1jeralAldeia/<id>',views.reportb1jeralAldeia, name='reportb1jeralAldeia'),
 

#relatorio jeral ba print
   path('reportb1_printjeral',views.reportb1_printjeral, name='reportb1_printjeral'),
   path('reportb1_printPostadministrative/<id>',views.reportb1_printPostadministrative, name='reportb1_printPostadministrative'),
   path('reportb1_printVillage/<id>',views.reportb1_printVillage, name='reportb1_printVillage'),



# Temporario
   path('temporary/',views.temporary_list, name='temporary'),
   path('temporary_input/',views.temporary_input, name='temporary_input'),
   path('temporary_update/<hashed>',views.temporary_update, name='temporary_update'),
   path('temporary_delete/<hashed>',views.temporary_delete, name='temporary_delete'),
   

#custom data


   path('municipality/',views.municipality_list, name='municipality'),
   path('municipality_input/',views.municipality_input, name='municipality_input'),
   path('municipality_edit/<id>',views.municipality_edit, name='municipality_edit'),
   path('municipality_delete/<id>',views.municipality_delete, name='municipality_delete'),

   path('administrativepost/',views.administrativepost_list, name='administrativepost'),
   path('administrativepost_input/',views.administrativepost_input, name='administrativepost_input'),
   path('administrativepost_edit/<id>',views.administrativepost_edit, name='administrativepost_edit'),
   path('administrativepost_delete/<id>',views.administrativepost_delete, name='administrativepost_delete'),


   path('village/',views.village_list, name='village'),
   path('village_input/',views.village_input, name='village_input'),
   path('village_edit/<id>',views.village_edit, name='village_edit'),
   path('village_delete/<id>',views.village_delete, name='village_delete'),


   path('aldeia/',views.aldeia_list, name='aldeia'),
   path('aldeia_input/',views.aldeia_input, name='aldeia_input'),
   path('aldeia_edit/<id>',views.aldeia_edit, name='aldeia_edit'),
   path('aldeia_delete/<id>',views.village_delete, name='aldeia_delete'),




   path('citizen/',views.citizen_list, name='citizen'),
   path('citizen_input/',views.citizen_input, name='citizen_input'),
   path('citizen_edit/<id>',views.citizen_edit, name='citizen_edit'),
   path('citizen_delete/<id>',views.citizen_delete, name='citizen_delete'),


   path('religion/',views.religion_list, name='religion'),
   path('religion_input/',views.religion_input, name='religion_input'),
   path('religion_edit/<id>',views.religion_edit, name='religion_edit'),
   path('religion_delete/<id>',views.religion_delete, name='religion_delete'),


   path('profession/',views.profession_list, name='profession'),
   path('profession_input/',views.profession_input, name='profession_input'),
   path('profession_edit/<id>',views.profession_edit, name='profession_edit'),
   path('profession_delete/<id>',views.profession_delete, name='profession_delete'),


   path('level_education/',views.level_education_list, name='level_education'),
   path('level_education_input/',views.level_education_input, name='level_education_input'),
   path('level_education_edit/<id>',views.level_education_edit, name='level_education_edit'),
   path('level_education_delete/<id>',views.level_education_delete, name='level_education_delete'),


   
   path('familyposition/',views.familyposition_list, name='familyposition'),
   path('familyposition_input/',views.familyposition_input, name='familyposition_input'),
   path('familyposition_edit/<id>',views.familyposition_edit, name='familyposition_edit'),
   path('lfamilyposition_delete/<id>',views.familyposition_delete, name='familyposition_delete'),

   path('popchar_genderyear',views.popchar_genderyear, name='popchar_genderyear'),
   path('popchar_changes',views.popchar_changes, name='popchar_changes'),
   path('popchar_temporary',views.popchar_temporary, name='popchar_temporary'),


   path('popchar_munisipality',views.popchar_munisipality, name='popchar_munisipality'),
   path('popchar_postadministrative/<id>',views.popchar_postadministrative, name='popchar_postadministrative'),
   path('popchar_village/<id>',views.popchar_village, name='popchar_village'),
   path('popchar_aldeia/<id>',views.popchar_aldeia, name='popchar_aldeia'),



#FXA FAMILIA ONLINE

   path('familycard_list/',views.familycard_list, name='familycard_list'),

   path('registerfamilycard/<hashed>',views.registerfamilycard, name='registerfamilycard'),

   path('resetpassword/<hashed>',views.resetpassword, name='resetpassword'),

   path('updatefamilycard/<hashed>',views.updatefamilycard, name='updatefamilycard'),


#mudansa populasaun / migrations

#mudansa populasaun sai


#mudansa populasaun tama

   # path('entermigration/',views.entermigration_list, name='entermigration'),
   # path('entermigration_input/',views.entermigration_input, name='entermigration_input'),
   # # path('entermigration_update/<hashed>',views.entermigration_update, name='entermigration_update'),

   # #populasaun mudansa tama
   # path('migration_input/<hashed>',views.migration_input, name='migration_input'),
   



   


]