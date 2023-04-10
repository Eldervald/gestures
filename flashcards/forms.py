from django.forms import ModelForm
from django import forms
from .models import Card_Set, Card

class Card_Set_Form(ModelForm):
    class Meta:
        model = Card_Set
        fields = ['topic', 'description']


class Card_Form(ModelForm):
    class Meta:
        model = Card
        fields = ['parent_card_set', 'video', 'definition']



