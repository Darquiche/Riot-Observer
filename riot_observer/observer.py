# -*- coding: utf-8 -*-
"""
Riot Observer
~~~~~~~~~~~~~~~~~~~

A light wrapper for the RiotGames API.
Based on RiotWatcher by pseudonym117
https://github.com/pseudonym117/Riot-Watcher

Updated to v3 endpoints by Darqi

:copyright: (c) 2015-2016 pseudonym117
:copyright: (c) 2017 Darqi
:license: MIT, see LICENSE for more details.

"""

__title__ = 'RiotObserver'
__author__ = 'Darqi'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 Darqi'
__version__ = '1.3.3'

from collections import deque
import time
import requests
from riot_observer import constants as c

api_versions = {
    'champion': 3,
    'spectator': 3,
    'match': 3,
    'league': 3,
    'lol-static-data': 3,
    'lol-status': 3,
    'summoner': 3,
    'champion-mastery': 3,  #not yet implemented
    'masteries': 3,         #not yet implemented
    'runes': 3,             #not yet implemented
}


class LoLException(Exception):
    def __init__(self, error, response):
        self.error = error
        self.headers = response.headers

    def __str__(self):
        return self.error

    def __eq__(self, other):
        if isinstance(other, "".__class__):
            return self.error == other
        elif isinstance(other, self.__class__):
            return self.error == other.error and self.headers == other.headers
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return super(LoLException).__hash__()


error_400 = "Bad request"
error_401 = "Unauthorized"
error_403 = "Blacklisted key"
error_404 = "Game data not found"
error_405 = "Method not allowed"
error_415 = "Unsupported media type"
error_422 = "Player exists, but hasn't played since match history collection began"
error_429 = "Too many requests"
error_500 = "Internal server error"
error_502 = "Bad gateway"
error_503 = "Service unavailable"
error_504 = 'Gateway timeout'


def raise_status(response):
    if response.status_code == 400:
        raise LoLException(error_400, response)
    elif response.status_code == 401:
        raise LoLException(error_401, response)
    elif response.status_code == 403:
        raise LoLException(error_403, response)
    elif response.status_code == 404:
        raise LoLException(error_404, response)
    elif response.status_code == 405:
        raise LoLException(error_405, response)
    elif response.status_code == 415:
        raise LoLException(error_415, response)
    elif response.status_code == 422:
        raise LoLException(error_422, response)
    elif response.status_code == 429:
        raise LoLException(error_429, response)
    elif response.status_code == 500:
        raise LoLException(error_500, response)
    elif response.status_code == 502:
        raise LoLException(error_502, response)
    elif response.status_code == 503:
        raise LoLException(error_503, response)
    elif response.status_code == 504:
        raise LoLException(error_504, response)
    else:
        response.raise_for_status()


class RateLimit:
    def __init__(self, allowed_requests, seconds):
        self.allowed_requests = allowed_requests
        self.seconds = seconds
        self.made_requests = deque()

    def __reload(self):
        t = time.time()
        while len(self.made_requests) > 0 and self.made_requests[0] < t:
            self.made_requests.popleft()

    def add_request(self):
        self.made_requests.append(time.time() + self.seconds)

    def request_available(self):
        self.__reload()
        return len(self.made_requests) < self.allowed_requests


class RiotObserver:
    def __init__(self, key, default_region=(c.EUROPE_WEST), limits=(RateLimit(10, 10), RateLimit(500, 600), )):
        self.key = key  #If you have a production key, use limits=(RateLimit(3000,10), RateLimit(180000,600),)
        self.default_region = default_region
        self.limits = limits

    def can_make_request(self):
        for lim in self.limits:
            if not lim.request_available():
                return False
        return True

    def base_request(self, url, region, static=False, **kwargs):
        if region is None:
            region = self.default_region
        args = {'api_key': self.key}
        for k in kwargs:
            if kwargs[k] is not None:
                args[k] = kwargs[k]
        r = requests.get(
            'https://{region}.api.riotgames.com/lol/{static}{url}'.format(
                region=region,
                static='static-data/' if static else '',
                url=url,
            ),
            params=args
        )
        #print(r.url)
        if not static:
            for lim in self.limits:
                lim.add_request()
        raise_status(r)
        return r.json()

    @staticmethod
    def sanitized_name(name):
        return name.replace(' ', '').lower()

    # champion-v3
    def _champion_request(self, end_url, region, **kwargs):
        return self.base_request(
            'platform/v{version}/champions{end_url}'.format(
                version=api_versions['champion'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_all_champions(self, region=None, free_to_play=False):
        if free_to_play == True:
            free_to_play = "true"
        else:
            free_to_play = "false"
        return self._champion_request('', region, freeToPlay=free_to_play)

    def get_champion(self, champion_id, region=None):
        return self._champion_request('/{id}'.format(id=champion_id), region)

    # spectator-v3
    def _spectator_request(self, end_url, region, **kwargs):
        return self.base_request(
            'spectator/v{version}/{end_url}'.format(
                version=api_versions['spectator'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_current_game(self, summoner_id, region=None):
        return self._spectator_request('active-games/by-summoner/{id}'.format(id=summoner_id), region)

    def get_featured_games(self, region=None):
        return self._spectator_request('featured-games', region)

    # match-v3
    def _match_request(self, end_url, region, **kwargs):
        return self.base_request(
            'match/v{version}/{end_url}'.format(
                version=api_versions['match'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_match(self, match_id, region=None):
        return self._match_request('matches/{id}'.format(id=match_id), region)

    #def get_matchlist(self, account_id, region=None):
    #    return self._match_request('matchlists/by-account/{id}'.format(id=account_id), region)

    def get_matchlist(self, account_id, region=None, queue_ids=None, begin_time=None, end_index=None, season_ids=None, champion_ids=None, begin_index=None, end_time=None):
        if queue_ids is not None and not isinstance(queue_ids, str) :
            queue_ids = ','.join(queue_ids)
        if season_ids is not None and not isinstance(season_ids, str):
            season_ids = ','.join(season_ids)
        return self._match_request(
            'matchlists/by-account/{id}'.format(id=account_id),
            region,
            queue=queue_ids,
            beginTime=begin_time,
            endIndex=end_index,
            season=season_ids,
            champion=champion_ids,
            beginIndex=begin_index,
            endTime=end_time
        )

    def get_recent_matchlist(self, account_id, region=None):
        return self._match_request('matchlists/by-account/{id}/recent'.format(id=account_id), region)

    def get_timeline(self, match_id, region=None):
        return self._match_request('timelines/by-match/{id}'.format(id=match_id), region)

    def get_matches_tournament(self, tournament_code, region=None):
        return self._match_request('matches/by-tournament-code/{code}/ids'.format(code=tournament_code), region)

    def get_match_tournament(self, match_id, tournament_code, region=None):
        return self._match_request('matches/{id}/by-tournament-code/{code}'.format(id=match_id, code=tournament_code), region)

    # league-v3
    def _league_request(self, end_url, region, **kwargs):
        return self.base_request(
            'league/v{version}/{end_url}'.format(
                version=api_versions['league'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_challenger(self, region=None, queue=c.ranked_solo):
        return self._league_request('challengerleagues/by-queue/{q}'.format(q=queue), region)

    def get_league(self, summoner_id, region=None):
        return self._league_request('leagues/by-summoner/{id}'.format(id=summoner_id), region)

    def get_master(self, region=None, queue=c.ranked_solo):
        return self._league_request('masterleagues/by-queue/{q}'.format(q=queue), region)

    def get_position(self, summoner_id, region=None):
        return self._league_request('positions/by-summoner/{id}'.format(id=summoner_id), region)

    # lol-static-data-v3
    def _static_request(self, end_url, region, **kwargs):
        return self.base_request(
            'v{version}/{end_url}'.format(
                version=api_versions['lol-static-data'],
                end_url=end_url
            ),
            region,
            static=True,
            **kwargs
        )

    def static_get_champion_list(self, region=None, champ_list_data=None, tags=None, version=None, data_by_id=None, locale=None):
        return self._static_request(
            'champions',
            region,
            champListData=champ_list_data,
            tags=tags,
            version=version,
            dataById=data_by_id,
            locale=locale
        )

    def static_get_champion(self, champ_id, region=None, champ_data=None, tags=None, version=None, locale=None):
        return self._static_request(
            'champions/{id}'.format(id=champ_id),
            region,
            champData=champ_data,
            tags=tags,
            version=version,
            locale=locale
        )

    def static_get_item_list(self, region=None, item_list_data=None, tags=None, version=None, locale=None):
        return self._static_request(
            'items',
            region,
            itemListData=item_list_data,
            tags=tags,
            version=version,
            locale=locale
        )

    def static_get_item(self, item_id, region=None, item_data=None, tags=None, version=None, locale=None):
        return self._static_request(
            'items/{id}'.format(id=item_id),
            region,
            itemData=item_data,
            tags=tags,
            version=version,
            locale=locale
        )

    def static_get_language_strings(self, region=None, version=None, locale=None):
        return self._static_request(
            "language-strings",
            region,
            version=version,
            locale=locale
        )

    def static_get_languages(self, region=None):
        return self._static_request(
            "languages",
            region
        )

    def static_get_maps(self, region=None, version=None, locale=None):
        return self._static_request(
            "maps",
            region,
            version=version,
            locale=locale
        )

    def static_get_mastery_list(self, region=None, version=None, tags=None, locale=None):
        return self._static_request(
            "masteries",
            region,
            version=version,
            tags=tags,
            locale=locale
        )

    def static_get_mastery(self, mastery_id, region=None, version=None, tags=None, locale=None):
        return self._static_request(
            'masteries/{id}'.format(id=mastery_id),
            region,
            version=version,
            tags=tags,
            locale=locale
        )

    def static_get_icons(self, region=None, version=None, locale=None):
        return self._static_request(
            "profile-icons",
            region,
            version=version,
            locale=locale
        )

    def static_get_realm(self, region=None):
        return self._static_request('realms', region)

    def static_get_rune_list(self, region=None, version=None, tags=None, locale=None):
        return self._static_request(
            "runes",
            region,
            version=version,
            tags=tags,
            locale=locale
        )

    def static_get_rune(self, rune_id, region=None, version=None, tags=None, locale=None):
        return self._static_request(
            'runes/{id}'.format(id=rune_id),
            region,
            version=version,
            tags=tags,
            locale=locale
        )

    def static_get_summoner_spell_list(self, region=None, version=None, data_by_id=None, tags=None, locale=None):
        return self._static_request(
            "summoner-spells",
            region,
            version=version,
            dataById=data_by_id,
            tags=tags,
            locale=locale
        )

    def static_get_summoner_spell(self, spell_id, region=None, version=None, tags=None, locale=None):
        return self._static_request(
            'summoner-spells/{id}'.format(id=spell_id),
            region,
            version=version,
            tags=tags,
            locale=locale
        )

    def static_get_versions(self, region=None):
        return self._static_request('versions', region)

    # lol-status-v3
    def _status_request(self, end_url, region, **kwargs):
        return self.base_request(
            'status/v{version}/{end_url}'.format(
                version=api_versions['lol-status'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_shard_data(self, region=None):
        return self._status_request('shard-data', region)

    # summoner-v3
    def _summoner_request(self, end_url, region, **kwargs):
        return self.base_request(
            'summoner/v{version}/{end_url}'.format(
                version=api_versions['summoner'],
                end_url=end_url
            ),
            region,
            **kwargs
        )

    def get_summoner_by_id(self, summoner_id, region=None):
        return self._summoner_request('summoners/{id}'.format(id=summoner_id), region)

    def get_summoner_by_accountid(self, account_id, region=None):
        return self._summoner_request('summoners/by-account/{id}'.format(id=account_id), region)

    def get_summoner_by_name(self, summoner_name, region=None):
        return self._summoner_request('summoners/by-name/{name}'.format(name=self.sanitized_name(summoner_name)), region)
