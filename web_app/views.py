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
def match_detail(request, match_id):
    match = models.get_details_match(match_id)
    return render(request, 'web_app/match_detail.html', {
        'match': match
    })


def player_detail(request, player_id):
    acc = models.get_account(int(player_id))
    models.DetailMatchPlayer.objects.aggregate()
    raw = models.Account.objects.raw(
        'SELECT dmp2.player_account_id as id,  count(*) as qtd    FROM web_app_account acc   JOIN web_app_detailmatchplayer dmp1 ON acc.id = dmp1.player_account_id   JOIN web_app_detailmatchplayer dmp2 ON dmp1.match_id = dmp2.match_id WHERE dmp1.player_account_id = '+str(acc.id)+' and dmp2.player_account_id <> '+str(acc.id)+' GROUP BY dmp1.player_account_id,dmp2.player_account_id HAVING qtd > 10 ORDER BY qtd   DESC ')
    return render(request, 'web_app/account.html', {
        'account': acc,
        'friends': raw

    })


def friends_detail(request, players):
    accounts_ids = players.split("/")[:-1]
    matches = models.DetailMatch.objects
    for account_id in accounts_ids:
        matches = matches.filter(players__player_account__account_id=account_id)
    matches.select_related('players')
    return render(request, 'web_app/friend_matches.html', {
        'accounts' : models.Account.objects.filter(account_id__in=accounts_ids),
        'matches': matches
    })