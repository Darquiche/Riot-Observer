# Riot-Observer **v1.3.3**

Riot-Observer is a light wrapper of the [Riot Games API for League of Legends](https://developer.riotgames.com/). With the release of the v3 endpoints and the [API Versioning and deprecation policy](https://developer.riotgames.com/api-versioning.html/), major part of old methods are deprecated from **7/24/17**. Based on the pseudonym117's work [RiotWatcher](https://github.com/pseudonym117/Riot-Watcher), I tried to update all
the methods. All game constants are also included in variable file. Requests are kept track of so that you can stay below your rate limit. The default rate limits are set to 10 requests every 10 seconds and 500 requests every 10 minutes (the limit for development keys). The rate limiter does not prevent you from making requests that will be blocked and cause an exception, it simply allows you to check if you request will go through.

### Summary
- [API Versions](#api-versions)
- [Getting started](#getting-started)
- [Usage](#usage)
- [Testing](#testing)
- [Changelog](#changelog)

### API Versions
API | Version | Supported
----|---------|-----------
champion | v3 | v3
spectator | v3 | v3
match | v3 | v3
league | v3 | v3
lol-static-data | v3 | v3
lol-status | v3 | v3
summoner | v3 | v3
champion-mastery | v3 | *not yet implemented*
masteries | v3 | *not yet implemented*
runes | v3 | *not yet implemented*

### Getting started

To install Riot-Observer:

``
pip install riot_observer
``

OR:

``Python
python setup.py install
``

You also need to have an API key from Riot. Get that from
[here](https://developer.riotgames.com/).

### Usage

All methods return dictionaries representing the json objects described
by the official [Riot API](https://developer.riotgames.com/api-methods/). Any error (e.g. 404) that are known to the
service are returned as custom objects (error_404, error_500, ...),
for you to deal with however you like. Any other HTTP errors that are
not known returns of the API are raised as exceptions as in the Requests
API.

Default region of this application is EUW, but that can be changed during
initialization.

```Python

from riot_observer import RiotObserver

w = RiotObserver('<your-api-key>')

# check if we have API calls remaining
print(w.can_make_request())

# Get summoner's infos
a_guy = w.get_summoner_by_name(summoner_name='Puchi Otaku')
print(a_guy)

# Get summoner's ranked matches
ranked_games = w.get_matchlist(account_id=a_guy['accountId'])
print(ranked_games)

# all static methods are prefaced with 'static'
# static requests do not count against your request limit
# but at the same time, they don't change often...
static_champ_list = w.static_get_champion_list()
print(static_champ_list)

# import constants like region codes, or game constants
from riot_observer import constants as c

# request data from NA
creator = w.get_summoner_b(summoner_name='pseudonym117', region=c.NORTH_AMERICA)
print(creator)

# create watcher with NA as its default region
na = RiotObserver('<your-api-key>', default_region=c.NORTH_AMERICA)

# proper way to send names with spaces is to remove them, still works with spaces though (the wrapper includes a sanitize function)
xpeke = w.get_summoner(name='fnaticxmid')
print(xpeke)

# Error checking requires importing LoLException as well as any errors you wish to check for.
# For Riot's API, the 404 status code indicates that the requested data wasn't found and
# should be expected to occur in normal operation, as in the case of a an invalid summoner name,
# match ID, etc.
# The 429 status code indicates that the user has sent too many requests
# in a given amount of time ("rate limiting").

from riot_observer import LoLException
from riot_observer.observer import error_404, error_429

try:
  response = w.get_summoner_by_name('a dude')
except LoLException as e:
  if e == error_429:
      print('We should retry in {} seconds.'.format(e.headers['Retry-After']))
  elif e == error_404:
      print('Summoner not found.')

```

I'm writing a full API reference with all available methods in this wrapper.

### Testing

The tests included are not perfect, and don't have full code
coverage, but they should detect most issues.
To run these tests (to make sure its the API f-ing up not your code):

- Run **test.py** and enter your API key
- Enter a summoner name
- Then just follow the instructions ("Press enter to continue...", it's not too difficult)
- You can modify the test.py file to test more methods!

### Changelog

Riot-Observer's changelog
```
v1.3.3 - 06/11/2017

Endpoints updates:
 - updated champion API to v3
 - updated spectator API to v3
 - updated match API to v3
 - updated league API to v3
 - updated lol-static-data API to v3
 - updated lol-status API to v3
 - updated summoner API to v3

Methods added and modified.
Full documentation coming soon.
```

RiotWatcher's changelog
```
v1.3.2 - 11/16/2015

fixed issue with special characters in names in get_summoners method (issue #28)

fixed bug in matchlist API causing requests for past seasons to fail,
added constants for each possible season. (issue #44)

fixed bug introduced in pull request #35
(method of checked for what exception is thrown changed from what was documented) - old method should work now. (issue #43)

v1.3.1 - 10/24/2015

removed match history functions, as these were deprecated.

v1.3 - 7/29/2015

merged pull requests to (done at previous date, changelog not updated):
 - use matchlist endpoint
 - use nemesis draft
 - use riot attribution
 - get master tier

fixed issue with merged matchlist endpoint tests
fixed issue #24 in readme
added black market brawlers constants

v1.2.5 - 3/8/2015

fixed issue with __init__.py not importing the correct packages

v1.2.4 - 2/13/2015

Added current-game-v1.0 and featured-games-v1.0 api's

v1.2.3 - 12/31/2014

Fixed bug/undocumented feature when getting a single summoner with space
in the name. Also added static method
``RiotWatcher.sanitize_name(name)`` for stripping special characters
from summoner names.

v1.2.2 - 12/22/2014

Tiny changes, function signature of get\_summoner changed, to get by ID
the keyword is now ``_id``, not ``id``, tests updated to reflect this

Some game constants updated, if anyone has actually been using them.

v1.2.1 - 10/14/2014

Add lol-status API. not a huge thing but i had time to do it.

v1.2 - 9/4/2014

Added Match and MatchHistory APIs! Also are somewhat tested, but query
parameters are not tested.

Added some new constants. Probably not useful, but who knows. Maybe
someone will want them.

Some code changed to look slightly nicer too.

v1.1.8 - 9/4/2014

Updated APIs supported. Updated APIs:

-  league-v2.5
-  team-v2.4

Don't worry, support for match data is coming. I just wanted to commit
these changes first, since they already had tests.

v1.1.7 - 8/10/2014

Fixed issue #4 (forgot to change a number, oops) and made it much much
less likely for me to do it again (moved api version part of url into a
different method just to be sure I don't mess it up).

Also there are now TESTS!! WOO! Everyone rejoice. They aren't very good
tests though, so don't be too excited. BUT if they should detect if
there's a clear issue in the API wrapper.

Oh and some better formatting done (spaces not tabs, more consistent
indentation, etc.). Should be no functional difference at all.

v1.1.6 - 6/19/2014

Added support for regional proxies, because EUW broke without it

v1.1.5 - 5/9/2014

Cause what do version numbers really mean anyways?

Actually add endpoints to league API that I just forgot to add. Change
is NOT backwards compatible, any use of the old league api calls will
need to be changed, in addition to the riot changes.

Newly supported API's: - league-v2.4 - team-v2.3

v1.1.1 - 5/3/2014

Fix issue with static calls, namely that they didn't do anything right
before. Now they work.

v1.1 - 4/29/2014

Updated to latest API versions, now supported API's are:

-  champion-v1.2
-  game-v1.3
-  league-v2.3
-  lol-static-data-v1.2
-  stats-v1.3
-  summoner-v1.4
-  team-v2.2

Changes are NOT backwards compatible, you will need to update any code
that used an old API version. Check `Riots
documentation <https://developer.riotgames.com/change-history>`__ for
more information on what changes were made

v1.0.2 - 2/25/2014

Added Riots new methods to get teams by id. In methods
'get\_teams(team\_ids, region)' and 'get\_team(team\_id, region)'.

v1.0.1a

Alpha only, experimental rate limiting added

v1.0

Initial release
```

### Attribution

Riot-Observer isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing *League of Legends*. *League of Legends* and Riot Games are trademarks or registered trademarks of Riot Games, Inc. *League of Legends* (c) Riot Games, Inc.

Riot-Observer is based on [RiotWatcher](https://github.com/pseudonym117/Riot-Watcher) writing by ***pseudonym117***
