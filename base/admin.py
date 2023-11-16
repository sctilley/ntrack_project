from re import Match
from django.contrib import admin
from .models import League, MtgFormat, Archetype, Deck, League, Match

# Register your models here.
admin.site.register(MtgFormat)
admin.site.register(Archetype)
admin.site.register(Deck)
admin.site.register(League)
admin.site.register(Match)