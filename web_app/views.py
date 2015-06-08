# -*- coding: utf-8 -*-
from django.db import transaction
from django.shortcuts import render
from django.contrib import messages
import models
import dota2api
import logging
import os
import tasks
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


logger = logging.getLogger(__name__)

is_dev = os.environ.get('ENVIRONMENT', None)

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
        'SELECT dmp2.player_account_id as id,  count(*) as qtd    FROM web_app_account acc   JOIN web_app_detailmatchplayer dmp1 ON acc.id = dmp1.player_account_id   JOIN web_app_detailmatchplayer dmp2 ON dmp1.match_id = dmp2.match_id WHERE dmp1.player_account_id = ' + str(
            acc.id) + ' and dmp2.player_account_id <> ' + str(
            acc.id) + ' GROUP BY dmp1.player_account_id,dmp2.player_account_id HAVING count(*) > 1 ORDER BY count(*)   DESC'
    )
    return render(request, 'web_app/account.html', {
        'account': acc,
        'friends': raw

    })


def friends_detail(request, players):
    accounts_ids = players.split("/")[:-1]
    radiant_matches = models.DetailMatch.objects.distinct().order_by('-start_time')
    for account_id in accounts_ids:
        radiant_matches = radiant_matches.filter(players__player_account__account_id=account_id)

    matches_query = radiant_matches

    total_matches = len(matches_query)

    paginator = Paginator(matches_query, 25)
    page = request.GET.get('page')
    try:
        matches = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        matches = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        matches = paginator.page(paginator.num_pages)

    return render(request, 'web_app/friend_matches.html', {
        'accounts': models.Account.objects.filter(account_id__in=accounts_ids),
        'total_matches': total_matches,
        'matches': matches
    })


def download_games(request, player_id):
    try:
        if not is_dev:
            tasks.download_games(player_id)
        account = models.Account.objects.get(account_id=player_id)
        total_matches = models.get_total_matches_in_server(account)
        already_downloaded_games = len(account.match_players.all())
        matches_to_download = total_matches - already_downloaded_games

        if matches_to_download > 0:
            return JsonResponse({
                'type': 'success',
                'message': 'Started to download {} matches'.format(matches_to_download)
            })
        else:
            return JsonResponse({
                'type': 'success',
                'message': 'All matches synchronized'
            })
    except Exception as e:
        return JsonResponse({
            'type': 'error',
            'message': 'Erro: ' + e.message
        })

