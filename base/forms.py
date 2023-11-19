from django import forms
from django.forms import modelform_factory
from .models import Deck, League, Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = (
            'theirName',
            'theirArchetype',
            'theirDeck',
            'game1',
            'game2',
            'game3',
        )


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