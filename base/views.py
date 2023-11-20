from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django import forms
from django.forms import modelform_factory
from .models import Deck, League, Match
from .forms import DeckForm, LeagueForm, MatchForm

def clear_match(request, match_pk):
    match = Match.objects.get(pk=match_pk)
    match.theirName = None
    match.theirDeck = None
    match.theirArchetype = None
    match.game1 = False
    match.game2 = False
    match.game3 = None
    match.save()
    context = {
        'match':match
    }
    print("match cleared: ", match)

    return render(request, 'base/partials/match_row.html', context)

def test(request):
    context = {

    }

    return render(request, "base/test.html", context)

def edit_match(request, match_pk):
    match = Match.objects.get(pk=match_pk)
    context = {}
    context['match'] = match
    context['form'] = MatchForm(initial={
        'theirName':match.theirName,
        'theirArchetype': match.theirArchetype,
        'theirDeck': match.theirDeck,
        'game1': match.game1,
        'game2': match.game2,
        'game3': match.game3,
    })
    return render(request, 'base/partials/edit_match.html', context)

def edit_match_submit(request, match_pk):
    context = {}
    match = Match.objects.get(pk=match_pk)
    context['match'] = match
    if request.method == 'POST':
        print("post here22")
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            print("form valid")
            new_match = form.save(commit=False)
            print("request.POST:  ", request.POST)

            if new_match.game1 == 1:
                if new_match.game2 == 1:
                    new_match.didjawin = 1
                elif new_match.game3 == 1:
                    new_match.didjawin = 1
                else:
                    new_match.didjawin = 0
            elif new_match.game2 == 1:
                if new_match.game3 == 1:
                    new_match.didjawin = 1
                else:
                    new_match.didjawin = 0
            else:
                new_match.didjawin = 0
            
            new_match.save()
            league = League.objects.get(pk=new_match.league_id)
            total = 0
            for match in league.matches.all():
                if match.didjawin == True or match.didjawin == False:
                    total += 1
                else:
                    total += 0
            if total == 5:
                league.isFinished = True
                league.save()
                
        else:
            print("form not valid")
            return render(request, 'base/partials/match_row.html', context)

    print("cancel button") 
    return render(request, 'base/partials/match_row.html', context)


def home(request):
    user = request.user
    lform = LeagueForm()

    if request.method == 'POST':
        print("request.post trigger", request.POST)
        lform = LeagueForm(request.POST)
        if lform.is_valid():
            new_league = lform.save(commit=False)
            new_league.user = request.user
            new_league.save()

            user.profile.recentFormat = new_league.mtgFormat
            user.profile.recentDeck = new_league.myDeck
            user.profile.save()

            newleague = League.objects.latest('dateCreated')
            print("new league: ", newleague)

            for i in range(1,6):
                Match.objects.create(
                    league_id=new_league.pk,
                    user=user,
                    mtgFormat=new_league.mtgFormat,
                    myDeck=new_league.myDeck,
                    inLeagueNum=i,
                    didjawin=None
                )


        else:
            print("errors: ", lform.errors)
    context = {

    }
    return render(request, "base/home.html", context)



def get_matches_table(request, league_pk):
    league = League.objects.get(pk=league_pk)
    matches_list = league.matches.all()
    context = {
        "matches": matches_list
    }
    return render(request, 'base/partials/matches_table.html', context)

def get_league_current(request):
    leagues_list = League.objects.all().order_by('-dateCreated')

    current_league = League.objects.latest('dateCreated')
    matches_list = current_league.matches.all()



    if current_league.isFinished == True:
        pass
    #     context = {
    #     'lform':LeagueForm()
    # }
    #     return render(request, 'base/partials/add_league.html', context)
    else:
        context = {
            "cLeague": current_league,
            "matches": matches_list
        }
        return render(request, 'base/partials/current_matches.html', context)

def add_league(request):
    try:
        current_league = League.objects.filter(user=request.user).latest('dateCreated')
    except:
        current_league = League.objects.none()

    if current_league.isFinished == True:
        context = {
            'lform':LeagueForm()
        }
    else:
        context = {

        }


    return render(request, 'base/partials/add_league.html', context)
   
def get_leagues_accordion(request):
    leagues_list = League.objects.all().order_by('-dateCreated')
    context = {
        "leagues": leagues_list
    }
    return render(request, 'base/partials/league_accordion.html', context)

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

