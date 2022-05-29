from django import forms
from .models import Cards

class Add_card_to_deck(forms.ModelForm):
    class Meta():
        model = Cards
        fields = ['name_card', 'content']