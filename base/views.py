from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django import forms
from django.forms import modelform_factory
from .models import Deck
from .forms import DeckForm

def home(request):
    context = {

    }
    return render(request, "base/home.html", context)

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