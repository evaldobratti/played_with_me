# -*- coding: utf-8 -*-
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
import models
import dota2api
import logging


dota_api = dota2api.Initialise()

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return HttpResponse('HOHO HAHA')


@transaction.atomic
def match_details(request, match_id):
    get = models.DetailMatch.objects.filter(match_id=match_id)
    if get:
        print 'retrieving persisted'
        return HttpResponse('persisted' + str(get[0]))
    else:
        print 'getting from api'
        details = dota_api.get_match_details(match_id)
        print 'got! parsing'
        create = models.parse_from_details_match(details)
        return HttpResponse(create)
