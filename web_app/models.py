from django.db import models
from dota2api.api import *
import logging
import tasks
# Create your models here.
from django.db import transaction

dota_api = Initialise()


def get_until_success(get_function):
    while True:
        try:
            return get_function()
        except Exception as e:
            import logging

            logging.exception(e)


def get_account(account_id):
    steam_id = convert_to_64_bit(account_id)
    summaries = get_until_success(lambda: dota_api.get_player_summaries(steam_id))

    if summaries:
        account, account_created = Account.objects.get_or_create(account_id=account_id)
        account_response = summaries[0]

        account.community_visibility_state = account_response.community_visibility_state
        account.profile_state = account_response.profile_state
        account.persona_name = account_response.persona_name
        account.last_logoff = account_response.last_logoff
        account.profile_url = account_response.profile_url
        account.url_avatar = account_response.url_avatar
        account.url_avatar_medium = account_response.url_avatar_medium
        account.url_avatar_full = account_response.url_avatar_full
        account.persona_state = account_response.persona_state
        account.primary_clan_id = account_response.primary_clan_id
        account.time_created = account_response.time_created
        account.persona_state_flags = account_response.persona_state_flags
        account.save()
        return account

    return None


def get_details_match(match_id):
    match = DetailMatch.objects.filter(match_id=match_id)
    if match:
        return match[0]
    else:
        details = get_until_success(lambda: dota_api.get_match_details(match_id))
        return parse_from_details_match(details)


def load_team(match, players):
    for player_response in players:
        hero, hero_created = Hero.objects.get_or_create(hero_id=player_response.hero.id,
                                                        localized_name=player_response.hero.localized_name,
                                                        name=player_response.hero.name,
                                                        url_small_portrait=player_response.hero.url_small_portrait,
                                                        url_large_portrait=player_response.hero.url_large_portrait,
                                                        url_full_portrait=player_response.hero.url_full_portrait,
                                                        url_vertical_portrait=player_response.hero.url_vertical_portrait)

        account = get_account(player_response.account_id)

        player = DetailMatchPlayer.objects.create(match=match, player_account=account,
                                                  account_id=player_response.account_id,
                                                  player_slot=player_response.player_slot,
                                                  hero=hero, kills=player_response.kills,
                                                  deaths=player_response.deaths, assists=player_response.assists,
                                                  leaver_status=player_response.leaver_status,
                                                  gold=player_response.gold,
                                                  last_hits=player_response.last_hits, denies=player_response.denies,
                                                  gold_per_min=player_response.gold_per_min,
                                                  xp_per_min=player_response.xp_per_min,
                                                  gold_spent=player_response.gold_spent,
                                                  hero_damage=player_response.hero_damage,
                                                  tower_damage=player_response.tower_damage,
                                                  hero_healing=player_response.hero_healing,
                                                  level=player_response.level)

        for additional_unit in player_response.additional_units:
            unit, unit_created = AdditionalUnit.objects.get_or_create(unit_name=additional_unit.unit_name,
                                                                      player=player)
            for index, item_response in enumerate(additional_unit.items):
                item, item_created = Item.objects.get_or_create(item_id=item_response.id,
                                                                localized_name=item_response.localized_name,
                                                                name=item_response.name,
                                                                is_recipe=bool(item_response.is_recipe),
                                                                in_secret_shop=item_response.in_secret_shop,
                                                                cost=item_response.cost,
                                                                in_side_shop=item_response.in_side_shop,
                                                                url_image=item_response.url_image)

                DetailMatchOwnerItem.objects.create(owner=unit, slot=index, item=item)

        for index, item_response in enumerate(player_response.items):
            item, item_created = Item.objects.get_or_create(item_id=item_response.id,
                                                            localized_name=item_response.localized_name,
                                                            name=item_response.name,
                                                            is_recipe=bool(item_response.is_recipe),
                                                            in_secret_shop=item_response.in_secret_shop,
                                                            cost=item_response.cost,
                                                            in_side_shop=item_response.in_side_shop,
                                                            url_image=item_response.url_image)

            DetailMatchOwnerItem.objects.create(owner=player, slot=index, item=item)

        for upgrade in player_response.ability_upgrades:
            ability, ability_created = Ability.objects.get_or_create(ability_id=upgrade.ability,
                                                                     name=upgrade.ability_name)
            DetailMatchAbilityUpgrade.objects.create(player=player,
                                                     ability=ability,
                                                     time=upgrade.time,
                                                     upgraded_lvl=upgrade.level)


def parse_from_details_match(match_details):
    match = DetailMatch.objects.create(is_radiant_win=match_details.is_radiant_win, duration=match_details.duration,
                                       start_time=match_details.start_time, match_id=match_details.match_id,
                                       match_seq_num=match_details.match_seq_num,
                                       tower_status_radiant=match_details.tower_status_radiant,
                                       tower_status_dire=match_details.tower_status_dire,
                                       barracks_status_radiant=match_details.barracks_status_radiant,
                                       barracks_status_dire=match_details.barracks_status_dire,
                                       cluster=match_details.cluster,
                                       cluster_name=match_details.cluster_name,
                                       first_blood_time=match_details.first_blood_time,
                                       lobby_type=match_details.lobby_type, lobby_name=match_details.lobby_name,
                                       human_players=match_details.human_players, league_id=match_details.league_id,
                                       positive_votes=match_details.positive_votes,
                                       negative_votes=match_details.negative_votes,
                                       game_mode=match_details.game_mode, game_mode_name=match_details.game_mode_name)

    load_team(match, match_details.players)

    return match


class Account(models.Model):
    account_id = models.BigIntegerField(unique=True)
    steam_id = models.BigIntegerField(null=True)
    community_visibility_state = models.IntegerField(null=True)
    profile_state = models.IntegerField(null=True)
    persona_name = models.CharField(max_length=500, null=True)
    last_logoff = models.BigIntegerField(null=True)
    profile_url = models.CharField(max_length=500, null=True)
    url_avatar = models.CharField(max_length=500, null=True)
    url_avatar_medium = models.CharField(max_length=500, null=True)
    url_avatar_full = models.CharField(max_length=500, null=True)
    persona_state = models.IntegerField(null=True)
    primary_clan_id = models.BigIntegerField(null=True)
    time_created = models.BigIntegerField(null=True)
    persona_state_flags = models.BigIntegerField(null=True)


class Hero(models.Model):
    hero_id = models.SmallIntegerField()
    localized_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50, unique=True)
    url_small_portrait = models.CharField(max_length=300)
    url_large_portrait = models.CharField(max_length=300)
    url_full_portrait = models.CharField(max_length=300)
    url_vertical_portrait = models.CharField(max_length=300)


class Item(models.Model):
    item_id = models.SmallIntegerField(unique=True)
    localized_name = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    is_recipe = models.BooleanField()
    in_secret_shop = models.BooleanField()
    cost = models.SmallIntegerField()
    in_side_shop = models.BooleanField()
    url_image = models.CharField(max_length=400)


class Ability(models.Model):
    ability_id = models.SmallIntegerField()
    name = models.CharField(max_length=100)


class DetailMatch(models.Model):
    is_radiant_win = models.BooleanField()
    duration = models.BigIntegerField()
    start_time = models.BigIntegerField()
    match_id = models.BigIntegerField(unique=True)
    match_seq_num = models.BigIntegerField()
    tower_status_radiant = models.SmallIntegerField()
    tower_status_dire = models.SmallIntegerField()
    barracks_status_radiant = models.SmallIntegerField()
    barracks_status_dire = models.SmallIntegerField()
    cluster = models.IntegerField()
    cluster_name = models.CharField(max_length=50)
    first_blood_time = models.IntegerField()
    lobby_type = models.IntegerField()
    lobby_name = models.CharField(max_length=50)
    human_players = models.SmallIntegerField()
    league_id = models.BigIntegerField()
    positive_votes = models.IntegerField()
    negative_votes = models.IntegerField()
    game_mode = models.IntegerField()
    game_mode_name = models.CharField(max_length=50)


class ItemOwner(models.Model):
    pass


class DetailMatchPlayer(ItemOwner):
    player_account = models.ForeignKey(Account, null=True)
    match = models.ForeignKey(DetailMatch, null=False, related_name='players')
    account_id = models.BigIntegerField()
    player_slot = models.SmallIntegerField()

    hero = models.ForeignKey(Hero)

    kills = models.SmallIntegerField()
    deaths = models.SmallIntegerField()
    assists = models.SmallIntegerField()
    leaver_status = models.BooleanField()

    gold = models.IntegerField()
    last_hits = models.SmallIntegerField()
    denies = models.SmallIntegerField()
    gold_per_min = models.SmallIntegerField()
    xp_per_min = models.SmallIntegerField()
    gold_spent = models.IntegerField()
    hero_damage = models.IntegerField()
    tower_damage = models.IntegerField()
    hero_healing = models.IntegerField()
    level = models.IntegerField()


class AdditionalUnit(ItemOwner):
    unit_name = models.CharField(max_length=50)
    player = models.ForeignKey(DetailMatchPlayer, related_name="additional_units")


class DetailMatchOwnerItem(models.Model):
    slot = models.SmallIntegerField()
    owner = models.ForeignKey(ItemOwner, related_name="items")
    item = models.ForeignKey(Item)


class DetailMatchAbilityUpgrade(models.Model):
    player = models.ForeignKey(DetailMatchPlayer)
    ability = models.ForeignKey(Ability)
    time = models.IntegerField()
    upgraded_lvl = models.SmallIntegerField()
