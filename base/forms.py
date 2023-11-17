from django import forms
from django.forms import modelform_factory
from .models import Deck, League

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = (
            'name',
            'mtgFormat',
            'archetype'
        )

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = (
            'mtgFormat',
            'myDeck'
        )