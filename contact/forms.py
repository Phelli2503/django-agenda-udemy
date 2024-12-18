from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from contact.forms import ContactForm

from django.contrib.auth import password_validation


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ), required=False
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                 'class':'classe-a',
                 'placeholder':'INFORME SEU NOME',
            }
        ),
        label='PRIMEIRO NOME',
        # help_text='TEXTO DE AJUDA'
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
    first_name = forms.CharField(
        required=True,
        min_length=3, 
        widget=forms.TextInput(
            attrs={
                 'class':'classe-a',
                 'placeholder':'INFORME SEU NOME',
            }
        ),
        label='PRIMEIRO NOME',
    )
    last_name = forms.CharField(
        required=True,
        min_length=3, 
        widget=forms.TextInput(
            attrs={
                 'class':'classe-a',
                 'placeholder':'INFORME SEU SOBRENOME',
            }
        ),
        label='SOBRENOME',        
    )
    
    # email = forms.EmailField(
    #     required=True,
    # )

    class Meta:
        model = User
        fields = (
            'first_name','last_name','email',
            'username','password1','password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')

            )
        return email
    

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min-length': 'Por favor, adicione mais 2 letras'
        }
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label= 'Senha',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'nova-senha'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label= 'Repetir Senha',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'nova-senha'}),
        help_text='Digite a senha novamente',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 
        )


    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user       

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas diferentes')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email 

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este email', code='invalid')

                )

        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
           try:
               password_validation.validate_password(password1)
           except ValidationError as errors:
               self.add_error(
                   'password1',
                   ValidationError(errors),
               )
               
               

        return password1