from django import forms
from django.forms import modelform_factory
from .models import Deck, League, Match, Archetype

class MatchForm(forms.ModelForm):
    theirName = forms.CharField(required=True, max_length=100, label='test lable')
    theirArchetype = forms.ModelChoiceField(queryset=Archetype.objects.filter(mtgFormat=1).order_by('name'), label='Archetype', required=False)
    theirDeck = forms.ModelChoiceField(required=False, queryset=Deck.objects.filter(mtgFormat=1).order_by('name'), label='Their Deck')
    
    game1 = forms.BooleanField(label='one', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'largerCheckbox', 'title': 'This is game 1. Tick the box if you won.'}))
    game2 = forms.BooleanField(label='two', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'largerCheckbox', 'title': 'This is game 2. Tick the box if you won.'}))
    game3 = forms.BooleanField(label='three', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'largerCheckbox', 'title': 'This is game 3. Tick the box if you won.'}))

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