from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    import dota2api

    #players = dota2api.Initialise().get_match_details(1417434395).players
    return HttpResponse('rélo')