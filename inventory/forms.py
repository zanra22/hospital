import random
from django import forms
from inventory.models import Item, Drug

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'category', 'quantity')

class DrugForm(forms.ModelForm):

    class Meta:
        model = Drug
        fields = ('name', 'genericName', 'category', 'quantity')