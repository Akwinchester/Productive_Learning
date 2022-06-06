from django import forms
from .models import Cards, Decks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class Add_card_to_deck(forms.ModelForm):
#     class Meta():
#         model = Cards
#         fields = ['name_card', 'content']
#
# class Add_deck(forms.ModelForm):
#     class Meta():
#         model = Decks
#         fields = ['name_deck', 'id_category']


class Register_User(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password1', 'password2')