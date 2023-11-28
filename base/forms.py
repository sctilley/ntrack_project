from django import forms
from django.forms import modelform_factory
from .models import Deck, League, Match, Archetype, Flavor

class MatchForm(forms.ModelForm):
    theirName = forms.CharField(required=True, max_length=100, label='Their Name')
    theirDeck = forms.ModelChoiceField(required=False, queryset=Deck.objects.filter(mtgFormat=1).order_by('name'), label='Their Deck')
    theirFlavor = forms.ModelChoiceField(required=False, queryset=Flavor.objects.all().order_by('name'), label='Their Flavor')
    
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
            'theirFlavor',
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
            'myDeck',
            'myFlavor'
        )

class FlavorForm(forms.ModelForm):
    forms.ModelChoiceField(queryset=Flavor.objects.all(), label='Variant', widget=forms.Select(attrs={'disabled': 'disabled'}))
    name = forms.CharField(
        label="varient name", widget=forms.TextInput(attrs={'class': 'redtest2'}))
    isdefault = forms.BooleanField(label='Make Default Varient', required=False, widget=forms.CheckboxInput(
        attrs={'class': 'largerCheckbox'}))

    class Meta:
        model = Flavor
        fields = (
            'deck',
            'name',
            'isdefault',
        )

class TestForm(forms.Form):
    CHOICES= (
    ('ME', '1'),
    ('YOU', '2'),
    ('WE', '3'),
    )    
    field = forms.ChoiceField(choices=CHOICES)
