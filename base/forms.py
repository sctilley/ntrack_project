from django import forms
from django.forms import modelform_factory
from .models import Deck

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = (
            'name',
            'mtgFormat',
            'archetype'
        )
