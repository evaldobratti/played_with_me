from django.db import models
import logging
# Create your models here.


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

    for player_response in match_details.players:
        print 'parsing' + str(player_response)
        hero, hero_created = Hero.objects.get_or_create(hero_id=player_response.hero.id,
                                                        localized_name=player_response.hero.localized_name,
                                                        name=player_response.hero.name,
                                                        url_small_portrait=player_response.hero.url_small_portrait,
                                                        url_large_portrait=player_response.hero.url_large_portrait,
                                                        url_full_portrait=player_response.hero.url_full_portrait,
                                                        url_vertical_portrait=player_response.hero.url_vertical_portrait)

        player = DetailMatchPlayer.objects.create(match=match, account_id=player_response.account_id,
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

        for index, item_response in enumerate(player_response.items):
            item, item_created = Item.objects.get_or_create(item_id=item_response.id,
                                                            localized_name=item_response.localized_name,
                                                            name=item_response.name,
                                                            is_recipe=bool(item_response.is_recipe),
                                                            in_secret_shop=item_response.in_secret_shop,
                                                            cost=item_response.cost,
                                                            in_side_shop=item_response.in_side_shop,
                                                            url_image=item_response.url_image)

            DetailMatchPlayerItem.objects.create(player=player, slot=index, item=item)

        for upgrade in player_response.ability_upgrades:
            ability, ability_created = Ability.objects.get_or_create(ability_id=upgrade.ability,
                                                                     name=upgrade.ability_name)
            DetailMatchAbilityUpgrade.objects.create(player=player,
                                                     ability=ability,
                                                     time=upgrade.time,
                                                     upgraded_lvl=upgrade.level)

    return match


class UnsavedForeignKey(models.ForeignKey):
    allow_unsaved_instance_assignment = True


logger = logging.getLogger(__name__)


class Hero(models.Model):
    hero_id = models.SmallIntegerField()
    localized_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    url_small_portrait = models.CharField(max_length=300)
    url_large_portrait = models.CharField(max_length=300)
    url_full_portrait = models.CharField(max_length=300)
    url_vertical_portrait = models.CharField(max_length=300)


class Item(models.Model):
    item_id = models.SmallIntegerField()
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
    match_id = models.BigIntegerField()
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


class DetailMatchPlayer(models.Model):
    match = models.ForeignKey(DetailMatch)
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


class DetailMatchPlayerItem(models.Model):
    slot = models.SmallIntegerField()
    player = models.ForeignKey(DetailMatchPlayer)
    item = models.ForeignKey(Item)


class DetailMatchAbilityUpgrade(models.Model):
    player = models.ForeignKey(DetailMatchPlayer)
    ability = models.ForeignKey(Ability)
    time = models.IntegerField()
    upgraded_lvl = models.SmallIntegerField()


