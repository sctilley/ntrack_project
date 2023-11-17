from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django import forms
from django.forms import modelform_factory
from .models import Deck, League, Match
from .forms import DeckForm, LeagueForm

def add_league(request):
    context = {
        'lform':LeagueForm()
    }
    return render(request, 'base/partials/add_league.html', context)

def test(request):
    context = {

    }

    return render(request, "base/test.html", context)


def home(request):
    user = request.User
    lform = LeagueForm()
    print("home here")
    if request.method == 'POST':
        print("request.post trigger", request.POST)
        lform = LeagueForm(request.POST)
        if lform.is_valid():
            new_league = lform.save(commit=False)
            new_league.user = request.user
            new_league.save()

            user.profile.recentFormat = new_league.recentFormat
            user.profile.recentDeck = new_league.recentDeck
            user.profile.save()

            newleague = League.objects.latest('dateCreated')
            print("new league: ", newleague)


        else:
            print("errors: ", lform.errors)
    context = {

    }
    return render(request, "base/home.html", context)

def get_leagues_accordion(request):
    leagues_list = League.objects.all().order_by('-dateCreated')
    context = {
        "leagues": leagues_list
    }
    return render(request, 'base/partials/league_accordion.html', context)

def get_matches_table(request, league_pk):
    league = League.objects.get(pk=league_pk)
    matches_list = league.matches.all()
    context = {
        "matches": matches_list
    }
    return render(request, 'base/partials/matches_table.html', context)

def get_league_current(request):
    print("leagues got it")
    leagues_list = League.objects.all().order_by('-dateCreated')

    current_league = League.objects.latest('dateCreated')
    matches_list = current_league.matches.all()
    



    context = {
        "cLeague": current_league,
        "matches": matches_list
    }
    return render(request, 'base/partials/league_current.html', context)

@login_required
def decks(request):
    decks_list = Deck.objects.all().order_by('-dateCreated')
    print(decks_list)
    context = {
        "decks": decks_list
    }
    return render(request, 'base/decks.html', context)

def get_decks_list(request):
    print("got it")
    decks_list = Deck.objects.all().order_by('-dateCreated')
    context = {
        "decks": decks_list
    }
    return render(request, 'base/partials/decks_list.html', context)

def add_deck(request):
    context = {
        'form':DeckForm()
    }
    return render(request, 'base/partials/add_deck.html', context)

def submit_new_deck(request):
    form = DeckForm(request.POST)
    context = {
        'form':form
    }

    if form.is_valid():
        context['deck'] = form.save()
    else:
        print("form error")
        return redirect('home')

    
    return render(request, 'base/partials/deck_row.html', context)

def delete_deck(request, deck_pk):
    deck = Deck.objects.get(pk=deck_pk)
    deck.delete()
    return HttpResponse()

def edit_deck(request, deck_pk):
    deck = Deck.objects.get(pk=deck_pk)
    context = {}
    context['deck'] = deck
    context['form'] = DeckForm(initial={
        'name':deck.name,
        'mtgFormat': deck.mtgFormat,
        'archetype': deck.archetype,
    })
    return render(request, 'base/partials/edit_deck.html', context)

def edit_deck_submit(request, deck_pk):
    context = {}
    deck = Deck.objects.get(pk=deck_pk)
    context['deck'] = deck
    if request.method == 'POST':
        form = DeckForm(request.POST, instance=deck)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'base/partials/edit_deck.html', context)
        
    return render(request, 'base/partials/deck_row.html', context)

