# -*- coding: utf-8 -*-
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
import models
import dota2api
import logging




logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, 'web_app/index.html')


@transaction.atomic
def match_details(request, match_id):
    match = models.get_details_match(match_id)
    return render(request, 'web_app/match_detail.html', {
        'match': match
    })
