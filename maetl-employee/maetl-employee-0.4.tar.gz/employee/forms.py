from cProfile import label
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.db.models import Q
from django.contrib.auth.models import User, Group
from .models import Employee
from custom.models import *
class DateInput(forms.DateInput):
	input_type = 'date'

class EmployeeForm(forms.ModelForm):
	date_of_birth = forms.DateField(widget=DateInput(), required=False)
	start_period = forms.DateField(widget=DateInput(),label ='Mandatu Hahu', required=False)
	Group = [('xefe', 'Xefe Suku'), ('sec', 'PAAS') ]
	group_name = forms.ChoiceField(choices=Group, label='Naran Grupu')
	class Meta:
		model = Employee
		fields = ['first_name','last_name','phone_number','municipality','administrativepost','village','sex', 'group_name', 'start_period']
		labels = {
			'first_name': 'Naran Primeiru',
			'last_name': 'Apelidu',
			'phone_number': 'Númeru Telefone',
			'municipality': 'Munisípiu',
			'administrativepost': 'Postu Administrativu',
			'village': 'Suku',
			'sex': 'Seksu',
			'group_name': 'Naran Grupu',
			'start_period': 'Mandatu Hahú'
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('sex', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
			),
			Row(
                Column('group_name', css_class='form-group col-md-4 mb-0'),
				Column('phone_number', css_class='form-group col-md-4 mb-0'),
				Column('start_period', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('municipality', css_class='form-group col-md-3 mb-0'),
				Column('administrativepost', css_class='form-group col-md-3 mb-0'),
				Column('village', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit"> Chave <i class="fa fa-save"></i></button> """)
		)


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(required=False)
	class Meta:
		model = User
		fields = ['username','email']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('username', css_class='form-group col-md-6 mb-0'),
				Column('email', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-sm btn-info" type="submit">Save <i class="fa fa-save"></i></button> """)
		)