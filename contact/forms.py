from django import forms
from django.core.exceptions import ValidationError
from . import models

from django.contrib.auth.forms import UserCreationForm
# from contact.forms import ContactForm


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                 'class':'classe-a',
                 'placeholder':'INFORME SEU NOME',
            }
        ),
        label='PRIMEIRO NOME',
        help_text='TEXTO DE AJUDA'
    ) 

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs.update({
    #          'class':'classe-a',
    #          'placeholder':'INFORME SEU NOME',
    #     })

    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name','email','phone', 
            'email', 'description', 'category', 'picture',
                  )        
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'classe-a',
        #             'placeholder':'INFORME SEU NOME',
        #         }
        #     ),
        #     'email': forms.TextInput(
        #         attrs={
        #             'class':'classe-a',
        #             'placeholder':'INFORME SEU EMAIL',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao sobrenome',
                    code='invalid'
                )
                
            self.add_error(
                'last_name', msg
                )
            

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de Erro',
        #         code='invalid'
        #     )
        # )

        
        # self.add_error(
        #     None,
        #     ValidationError(
        #         'Mensagem de error: ',
        #         code='invalid'
        #     )
        # )

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite ABC neste campo',
                    code='invalid'
                )
            )
        
        return first_name

class RegisterForm(UserCreationForm):
    ...