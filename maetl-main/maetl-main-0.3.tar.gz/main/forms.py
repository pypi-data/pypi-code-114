from django import forms    
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomAuthenticationForm(AuthenticationForm):
    
    username = UsernameField(
        label='Usuariu',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'Itaboot nia naran Usuariu ou Password Sala'
        super().__init__(*args, **kwargs)
    