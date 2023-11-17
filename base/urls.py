from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('decks/', views.decks, name='decks'),
    path('test/', views.test, name='test'),
    path('get_decks_list', views.get_decks_list, name='get_decks_list'),
    path('add_deck', views.add_deck, name='add_deck'),
    path('add_league', views.add_league, name='add_league'),
    path('submit_new_deck', views.submit_new_deck, name='submit_new_deck'),
    path('<int:deck_pk>/delete_deck', views.delete_deck, name='delete_deck'),
    path('<int:deck_pk>/edit_deck', views.edit_deck, name='edit_deck'),
    path('<int:deck_pk>/edit_deck_submit', views.edit_deck_submit, name='edit_deck_submit'),
    path('get_league_current', views.get_league_current, name='get_league_current'),
    path('get_leagues_accordion', views.get_leagues_accordion, name='get_leagues_accordion'),
    path('<int:league_pk>/get_matches_table', views.get_matches_table, name='get_matches_table'),
]