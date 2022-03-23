from django import forms
from django.forms import ModelForm


from population.utils import *


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML,Field,Div
from crispy_forms.bootstrap import TabHolder,Tab
from django.db.models import Q
from custom.models import AdministrativePost, Village , Municipality, Village, Aldeia
from population.models import Population,Family,FamilyPosition,Level_Education,Temporary,Citizen,DetailFamily,Migration,Death,Migrationout,Religion,Profession,ChangeFamily

from datetime import datetime
from datetime import date
from django.utils import timezone

class Municipality_form(forms.ModelForm):
    class Meta:
        model = Municipality
        fields = ['id','name']


class AdministrativePost_form(forms.ModelForm):
    class Meta:
        model = AdministrativePost
        fields = ['id','name','municipality']


class Village_form(forms.ModelForm):
    class Meta:
        model = Village
        fields = ['id','name','administrativepost']

    def __init__(self, *args, **kwargs):
        super(Village_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'Detailfam'
        self.fields['administrativepost'].choices=[
     (item.pk, (str(item.name) + str(" / Munisipiu ") + str(item.municipality) )) for item in AdministrativePost.objects.all()]
        self.helper.layout = Layout(
        	Row(
				Column('name', css_class='form-group col-md-12 mb-0'), 
                Column('administrativepost', css_class='form-group col-md-12 mb-0'),          
				css_class='form-row'
			),

       

        )

class Aldeia_form(forms.ModelForm):
    class Meta:
        model = Aldeia
        fields = ['id','name','village']

    def __init__(self, *args, **kwargs):
        super(Aldeia_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'Detailfam'
        self.fields['village'].choices=[
     (item.pk, (str(item.name) + str(" / Postu  ") + str(item.administrativepost) + str(" / Munisípiu ") + str(item.administrativepost.municipality) )) for item in Village.objects.all()]
        self.helper.layout = Layout(
        	Row(
				Column('name', css_class='form-group col-md-12 mb-0'), 
                Column('village', css_class='form-group col-md-12 mb-0'),          
				css_class='form-row'
			),


        )

# class (forms.ModelForm):
#     class Meta:
#         model = Village
#         fields = ['id','name','administrativepost']




class FamilyPosition_form(forms.ModelForm):
    class Meta:
        model = FamilyPosition
        fields = ['id','name']

        

class FamilyPosition_form(forms.ModelForm):
    class Meta:
        model = FamilyPosition
        fields = ['id','name']


class Citizen_form(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = ['id','name']

class Religion_form(forms.ModelForm):
    class Meta:
        model = Religion
        fields = ['id','name']


class Profession_form(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ['id','name']

class Level_Education_form(forms.ModelForm):
    class Meta:
        model = Level_Education
        fields = ['id','name']



class Family_form(forms.ModelForm):
    data_registu = forms.DateField(label="Data Rejistu ",widget=forms.TextInput(attrs={'type': 'date' , 'min' : '2022-01-01'}))



    class Meta:
        model = Family
        fields = ['id_family','data_registu','aldeia']
    def __init__(self,site_id, *args, **kwargs):
        super(Family_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'id_form_email_verification'
        self.fields['aldeia'].choices=[
     (item.id, (str(item.name) )) for item in Aldeia.objects.filter(Q(village__id= site_id))]
        self.fields['id_family'].widget.attrs={'readonly':'readonly'}
        self.helper.layout = Layout(
			Row(
				Column('id_family', css_class ='form-group col-md-6 mb-0'), 
                Column('data_registu', css_class='form-group col-md-6 mb-0'),          
				css_class='form-row'
			), 

            		Row(
            Column('aldeia', css_class='form-group col-md-12 mb-0'),          
				css_class='form-row'
			), 
			HTML(""" 

            {% if action == 'input' %}

            <script type="text/javascript">
            var s = document.getElementById("id_id_family");
            s.value = "{{lastidfam}}";
                </script>

                    {% endif %}
                <hr><center>
                 <button class="btn btn-info" type="submit"><i class="fa fa-save"></i>  {% if action == 'input' %} Rai  {% elif action == 'edit' %} Atualiza Dadus {% endif %}</button> 
                 <a class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
                <center> """)
		)




class DetailFamily_form(forms.ModelForm):
    class Meta:
        model = DetailFamily
        fields = ['family_position']
        
#CustumDetailFamily_form utiliza hodi registu dados membru familia ida nia dados foti deit husi dados populasaun anterior
class CustumDetailFamily_form(forms.ModelForm):
    class Meta:
        model = DetailFamily
        fields = ['family_position','population']


    def __init__(self,site_id, *args, **kwargs):
        super(CustumDetailFamily_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'Detailfam'
        self.fields['population'].choices=[
     (item.id, (str(item.name) + str(" / Nu Bi : ") + str(item.nu_bi) )) for item in Population.objects.filter(Q(id_family='l') & Q(village__id = site_id) & Q(status_datap = 'ac'))]
        self.helper.layout = Layout(

                TabHolder(
                Tab('Rejistu dadus membru Foun',

                 Column( HTML("""

               
                <a href="{% url 'population:familymember_input' hashed %}"
              class="btn btn-labeled btn-info mb-2" type="button"> <span class="btn-label"><i class="fa fa-plus"></i></span>  Rejistu Membru Família </a>

              {% if check_chefe > 0 %} 

              <a href="{% url 'population:reportb5_print' hashed %}" target="__blank"
              class="btn btn-labeled btn-info mb-2" type="button"> <span class="btn-label"><i class="fa fa-print"></i></span> Print Fixa Família </a>

               {% endif %}
              
               """), css_class='form-group col-md-12 mb-0'), 
              ),

              Tab('Rejistu membru  bazeia ba dadus anterior',
              	Row(
               
            	Column('population', css_class='form-group col-md-6 mb-0'), 
            	Column('family_position', css_class='form-group col-md-3 mb-0'),
                Column(HTML("""   <label for='type_data' class=' requiredField'><span class='asteriskField'>*</span> </label><br><center><button  id = '' class="btn btn-info" type="submit"><i class="fa fa-save"></i>  Aumenta ba Membru Família </button>
                
                <center> """), css_class='form-group col-md-2 mb-0'), 
				css_class='form-row'
			), 
              
              )
                )
                
                )



class Death_form(forms.ModelForm):
    descriptiond = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)

    class Meta:
        model = Death
        fields = ['date','descriptiond']

        widgets = {
        'date' : forms.TextInput(
            attrs = {
                'class': 'form-control',
                'type': 'date',
                }),
        }
        
        

    def __init__(self, *args, **kwargs):
        super(Death_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'id_form_email_verification'
        self.helper.layout = Layout(
            
			Row(
            	Column('date', css_class='form-group col-md-12 mb-0'), 
            	Column('descriptiond', css_class='form-group col-md-12 mb-0'), 
				css_class='form-row'
			), 
            	
            HTML(""" <input type ='hidden' name='prosses' value='{{prosses}}'>
            
               <div class='float-right'>


   
            <button  id = 'submit_populationform' class="btn btn-info" type="submit"><i class="fa fa-save"></i>     Atualiza Dadus
               </button>

                   <a class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
    

          
             
             </div>
             
              """)
		)




class Migrationout_form(forms.ModelForm):
    descriptionmo = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)
    class Meta:
        model = Migrationout
        fields = ['date_migration','descriptionmo','to_aldeia','to_nation','cidadaunmo']
        widgets = {
        'date_migration' : forms.TextInput(
            attrs = {
                'class': 'form-control',
                'type': 'date',
                }),

        
             'cidadaunmo' : forms.Select(
        		attrs = {
        			'class': 'form-control',
        			'type': 'date',
                    'id': 'id_cidadaunmo',
                    'onchange' :'loadcolumn()'
                    }),

                 'to_aldeia' : forms.Select(
        		attrs = {
        		 'class': 'chosen',
                    }),


                    


        }


    def __init__(self,site_id, *args, **kwargs):
        super(Migrationout_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'id_form_email_verification'
        self.fields['to_aldeia'].choices=[
     (item.id, (str(item.name) +"/ Suku : " + str(item.village.name) + "/ Postu : " +  str(item.village.administrativepost.name) + "/ Munisipiu : " + str(item.village.administrativepost.municipality.name) )) for item in Aldeia.objects.exclude(village__id = site_id)]
        self.helper.layout = Layout(

        
            
			Row(

                Column('cidadaunmo', css_class='form-group col-md-12 mb-0'),
            	Column('to_aldeia', css_class='form-group col-md-12 mb-0',css_id='aldeia'), 
            	Column('to_nation', css_class='form-group col-md-12 mb-0',css_id='nation'), 
				css_class='form-row'
			), 
			Row(
            	Column('date_migration', css_class='form-group col-md-12 mb-0'), 
            	Column('descriptionmo', css_class='form-group col-md-12 mb-0'), 
				css_class='form-row'
			), 
            HTML("""
            {% load static %} 
               <script src="{% static 'main/vendor/choosen/choosen.js' %}"></script>
            
           
              <script type='text/javascript'>
             $(".chosen").chosen();
              </script>


            
             <input type ='hidden' name='prosses' value='{{prosses}}'>
            
            
               <div class='float-right'>

 

            <button  id = 'submit_populationform' class="btn btn-info" type="submit"><i class="fa fa-save"></i>  
            {% if prosses == 'edit' %} Atualiza Dadus {% else %}
             Rai {% endif %}
            
             </button>

                   <a class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
    

           
             <div>
             
             
             
                """)
		)


class Changefamily_form(forms.ModelForm):
    descriptioncf = forms.CharField(label="Observasun", widget=forms.Textarea(attrs={"rows":2}), required=False)
    class Meta:
        model = ChangeFamily
        fields = ['date_change','descriptioncf']
        widgets = {
        'date_change' : forms.TextInput(
            attrs = {
                'class': 'form-control',
                'type': 'date',
                }),
        }


    def __init__(self, *args, **kwargs):
        super(Changefamily_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'id_form_email_verification'
        self.helper.layout = Layout(
            
			Row(
            	Column('date_change', css_class='form-group col-md-12 mb-0'), 
            	Column('descriptioncf', css_class='form-group col-md-12 mb-0'), 
				css_class='form-row'
			), 
            HTML(""" 
                <div class='row float-right' >
                <input type ='hidden' name='prosses' value='{{prosses}}'><center><button  id = 'submit_populationform' class="btn btn-info" type="submit"><i class="fa fa-save"></i>  Atualiza Dadus </button>
       <a class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
              </div>

                 """)
		)






class Migration_form(forms.ModelForm):
    class Meta:
        from_aldeia = forms.ChoiceField(required=False)
        from_nation = forms.CharField(required=False)
        model = Migration
        fields = ['date_migration','cidadaunm','municipality','administrativepost','village','from_nation','from_aldeia']


        widgets = {
        'date_migration' : forms.TextInput(
        		attrs = {
        			'class': 'form-control',
        			'type': 'date',
                    }),
        
        'cidadaunm' : forms.Select(
        		attrs = {
        			'class': 'form-control',
        			'type': 'date',
                    'id': 'cidadaunm',
                    'onchange' :'loadcolumn()'
                    }),

        'municipality' : forms.Select(
                attrs = {
 
                    'type': 'text',
                    'id': 'id_municipality',
                    }),     

        'administrativepost' : forms.Select(
                attrs = {
 
                    'type': 'text',
                    'id': 'id_administrativepost',
                    }),     


        'village' : forms.Select(
                attrs = {
 
                    'type': 'text',
                    'id': 'id_village',
                    }),     


        'from_aldeia' : forms.Select(
                attrs = {
 
                    'type': 'text',
                    'id': 'from_aldeia',
                    }),     


                 


        'from_nation' : forms.TextInput(
        		attrs = {
        			'class': 'form-control',
        			'type': 'text',
                    'id': 'from_nation',
                    }),
        }




class Population_form(forms.ModelForm):

    imagen = forms.ImageField(required=False)
    descriptionp = forms.CharField(label="Observasaun", widget=forms.Textarea(attrs={"rows":2}), required=False)
    nu_bi = forms.CharField(label="Nú. Kartaun Identidade( BI )",required=False)
    
    class Meta:
        model = Population
        fields = ['name','place_of_bird','phone','date_of_bird','gender','vulnerable','marital_status','religion','date_register','descriptionp','imagen','citizenp','aldeia','nu_bi','deficient','nu_e','nu_p']



        widgets = {
        'date_of_bird' : forms.TextInput(
        		attrs = {
        			'class': 'form-control',
        			'type': 'date',
                    }),

        'date_register' : forms.TextInput(
        		attrs = {
        			'class': 'form-control',
        			'type': 'date',
                    }),

        }
    
    def __init__(self,site_id, *args, **kwargs):
        super(Population_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['aldeia'].choices=[
     (item.id, (str(item.name) )) for item in Aldeia.objects.filter(Q(village__id= site_id))]
        self.helper.form_id = 'populationform' #utiliza hodi halo validasaun ba form
        self.helper.layout = Layout(


            
                Column(HTML(""" 


                {% if prosses == 'registu' %}

                <label for='type_data' class=' requiredField'>Kategoria Populasaun <span class='asteriskField'>*</span> </label>
                <select id='type_data' name = 'type_data' onchange='loadform()' class='select form-control'>
                <option  value = 'popsuku'>Populasaun Orijinal Suku</option>
                <option value ='formmigration'>Populasaun Mudansa Tama</option>
                 </select>

                {% elif prosses == 'edit_pop' %}
             
                <label for='type_data' class=' requiredField'>Tipu Dadus <span class='asteriskField'>*</span> </label>
                <select id='type_data' name = 'type_data' onchange='loadform()' class='select form-control disable'>
                <option selected value = 'popsuku'>Populasaun Orijinal Suku </option>
                 </select>

                {% elif prosses == 'edit_mig' %}
                 
                <label for='type_data' class=' requiredField'>Tipu Dadus <span class='asteriskField'>*</span> </label>
                <select id='type_data' name = 'type_data' onchange='loadform()' class='select form-control disable'>
                <option selected value ='formmigration'>Populasaun Mudansa Tama </option>
                 </select>

                {% endif %}

                <br>
               
                 """), css_class='form-group col-md-12 mb-0'),
            TabHolder(

                Tab('Informasaun Pesoal',
                Row(
    
                Column('name', css_class='form-group  col-md-8 mb-0', css_id='name'),



                Column(
                    HTML(""" {% load crispy_forms_tags %} {{formdf|crispy}} """), css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
                ),

                Row(
                Column('date_of_bird', css_class='form-group col-md-4 mb-0'),
                Column('place_of_bird', css_class='form-group col-md-4 mb-0'),
                Column('aldeia', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
                ),

                Row(
                Column('gender', css_class='form-group col-md-4 mb-0'),
                Column('marital_status', css_class='form-group col-md-4 mb-0'),
                Column('religion', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			    ),

                Row(
                Column('nu_bi', css_class='form-group col-md-4 mb-0'),
                Column('nu_e', css_class='form-group col-md-4 mb-0'),
                Column('nu_p', css_class='form-group col-md-4 mb-0'),


				css_class='form-row'
                ),

                Row(
                Column('deficient', css_class='form-group col-md-4 mb-0'),
                Column('citizenp', css_class='form-group col-md-4 mb-0'),
                Column('phone', css_class='form-group col-md-4 mb-0'),             

                css_class='form-row'
                ),
                css_id='ip'),


    #             Tab('Estudu No servisu', 
    #             Row(
    #             Column('level_education', css_class='form-group col-md-12 mb-0'),
    #             Column('profession', css_class='form-group col-md-12 mb-0'),
				# css_class='form-row'),
    #             css_id='es'),
               
    #             Tab('Konhesemento Lingua',
    #             Column(
    #             Column('readalatin', css_class='form-group col-md-12 mb-0'),
    #             Column('readaarabe', css_class='form-group col-md-12 mb-0'),
    #             Column('readachina', css_class='form-group col-md-12 mb-0'),
				# css_class='form-row'
    #             ),
    #             css_id='kl'),

                Tab('Imagen', 
                Row(
                Column('imagen', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				css_class='form-row'),
                HTML(""" <center> <img id='output' width='200' /> </center> """),
                css_id='i'),

                Tab('Informasaun Seluk', 


       Row(

            
                Column('vulnerable', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'),

                Row(

                Column('date_register', css_class='form-group col-md-12 mb-0'),
              
				css_class='form-row',css_id='includedateregister'),
                Row(

                Column(HTML(""" 
                
                 {% if prosses == 'registu' %}





            <div id='includeformmigration'>


     


            {% load crispy_forms_tags %} {% load static %} 
            
            

        
              
            {{formm|crispy}}
            

             </div>
          <script src="{% static 'main/vendor/validation/migration-invalidtitle.js' %}"></script>

            
            

                {% elif prosses == 'edit_mig' %}
        
        
         <div id='includeformmigration'>
         

         {% load crispy_forms_tags %} {% load static %} 





         
         
         
         {{formm|crispy}} </div>
         <script src="{% static 'main/vendor/validation/migration-invalidtitle.js' %}"></script>

         

           

                {% endif %}
                
                 """), css_class='form-group col-md-12 mb-0'),


                Column('descriptionp', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'),

                
                 css_id='is'),
                


                ),


                 HTML(""" <br><center>
                 
                 <div class='float-right'>
                      <a href='#' onclick='validasaunform()'   id = 'submit_populationform' class="btn btn-info" ><i class="fa fa-save"></i> {% if prosses == 'registu' %} Rai {% else %} Atualiza Dadus{% endif %}  </a>
                    

             <a class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
    

             
               </div>


              
                   
         


                 <center> """)

              
                


		)	



class Population2_form(forms.ModelForm):


    
    class Meta:
        model = Population
        fields = ['level_education','profession']

    def __init__(self, *args, **kwargs):
        super(Population2_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'populationform' #utiliza hodi halo validasaun ba form
        self.helper.layout = Layout(


    



                Row(
                Column(HTML(""" <center><h4>Kompleta Formulariu</h4> </center> <hr>"""), css_class='form-group col-md-12 mb-0'),
                Column('level_education', css_class='form-group col-md-12 mb-0'),
                Column('profession', css_class='form-group col-md-12 mb-0'),
                Column(HTML(""" <br>

Koñesementu Lingua / Hili No Prenxe Lingua Ne’ebé Hatene <hr>

1.Lingua Internasional : <br><br>

{% for dados in language %}

 <input type="checkbox" {% if dados.hili == 'yes' %} checked {% endif %} id="vehicle" name='lingua' value="{{dados.id}}">
  <label for="vehicle1">{{dados.name}}</label>&nbsp; &nbsp; &nbsp;

{% endfor %}

<br> <br><br> 2.Lingua Materna : <br><br>
<textarea name="lingua_materna" cols="40" rows="2" class="textarea form-control" id="lingua_materna">
{{longuamat}}
</textarea>


                 
           
         


                  """), css_class='form-group col-md-12 mb-0'),

                css_class='form-row'),
             
 

                 HTML(""" <br><center>


                 
                 <div class='float-right'>



                          <button type='submit'  class="btn btn-info" ><i class="fa fa-save"></i>  Atualiza  Dadus </button>
                                            <a class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
    

               </div>


              
                   
         


                 <center> """)

              
                


        )   






class Temporary_form(forms.ModelForm):
     class Meta:
         
         model = Temporary
         fields = ['cidadaunt','from_place','purpose' ,'residence','date_arive','date_return','descriptionte']

         widgets = {




             
             'from_place' : forms.TextInput(
        		attrs = {
        			'class': 'form-control',
        			'id': 'hilialdeia',
                    }),



            
             'purpose' : forms.Textarea(
        		attrs = {
        			'class': 'form-control',
        			'cols': '3',
        			'rows': '1',
                    }),

             'residence' : forms.Textarea(
        		attrs = {
        			'class': 'form-control',
        			'cols': '3',
        			'rows': '1',
                    }),



             'date_arive' : forms.TextInput(
        		attrs = {
        			'class': 'form-control',
                    'type' : 'date'
                    }),

             'date_return' : forms.TextInput(
        		attrs = {
        			'class': 'form-control',
                    'type' : 'date'
                    }),


             'descriptionte' : forms.Textarea(
        		attrs = {
        			'class': 'form-control',
        			'cols': '3',
        			'rows': '1',
                    }),
                    
                    }        


              


class PopulationTemporary_form(forms.ModelForm):


    name = forms.CharField(label="Naran Kompletu",required=True)
    class Meta:
        model = Population
        fields = ['name','place_of_bird','date_of_bird','gender','profession','nu_bi','nu_p','nu_e','aldeia','deficient']

        widgets = {
        'date_of_bird' : forms.TextInput(
        		attrs = {
        			'class': 'form-control',
        			'type': 'date',
                    }),
        }
    
    def __init__(self,site_id, *args, **kwargs):
        super(PopulationTemporary_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['aldeia'].choices=[
     (item.id, (str(item.name) )) for item in Aldeia.objects.filter(Q(village__id= site_id))]
        self.helper.form_method = 'post'
        self.helper.form_id = 'temporaryform'
        
        # self.fields['aldeia'].choices=[(item.pk, (" Aldeia " + str(item.name) +" / Suku  " + str(item.village) + " / Postu "+ str(item.village.administrativepost) + " / Munisipiu " + str(item.village.administrativepost.municipality))) for item in Aldeia.objects.all()]

        self.helper.layout = Layout(


             Column(HTML(""" 
                <label for='type_data' class=' requiredField'>Kategoria Populasaun <span class='asteriskField'>*</span> </label>

                {% if prosses == 'te' %}

                   <select id='type_data' name = 'type_data' onchange='loadform()' class='select form-control'>
                <option  value = 'te' selected>Populasaun Temporáriu</option>
                 </select>

                {% elif prosses == 'mo' %}

                   <select id='type_data' name = 'type_data' onchange='loadform()' class='select form-control'>
                <option value ='mo'>Bebe Moris</option>
                 </select>

                {% else %}

                   <select id='type_data' name = 'type_data' onchange='loadform()' class='select form-control'>
                <option  value = 'te' selected>Populasaun Temporáriu</option>
                <option value ='mo'>Bebe Moris</option>
                 </select>

                {% endif %}
             
                <br> """), css_class='form-group col-md-12 mb-0'),


            TabHolder(


               
           

                Tab('Informasaun Personal',
                Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('gender', css_class='form-group col-md-4 mb-0'),
                Column('deficient', css_class='form-group col-md-4 mb-0'),


               
				css_class='form-row'
                ),

                Row(

                Column('place_of_bird', css_class='form-group col-md-6 mb-0'),
                Column('date_of_bird', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
                ),


                Row(
                Column('nu_bi', css_class='form-group col-md-4 mb-0'),
                Column('nu_p', css_class='form-group col-md-4 mb-0'),
                Column('nu_e', css_class='form-group col-md-4 mb-0'),
              
                css_class='form-row'
                ),

                Row(
                Column('profession', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			    ),
                css_id='ip'),



                
                Tab('Informasaun no razaun Mai iha suku', 

                Column('aldeia', css_class='form-group col-md-12 mb-0'),
                Column(
                Column(
                
                HTML("""{% load crispy_forms_tags %}
                 {% load static %} {{formtemp|crispy}}  
                    <script src="{% static 'main/vendor/validation/temporary-invalidtitle.js' %}"></script>
                """), css_class='form-group col-md-12 mb-0'),
				css_class='form-row'),
                css_id='ir'),

                ),

                 HTML(""" <br><center>
                 <div class='float-right'>

                      
                          <a href='#' onclick='validasaunformpoptemp()'   id = 'submit_populationtempform' class="btn btn-info" ><i class="fa fa-save"></i>  Rai </a>
                    <a class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Kansela</a>
           
               </div>


              
                   
         


                 <center> """),
		)	



