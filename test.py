import time

from riot_observer import RiotObserver
from riot_observer import LoLException
from riot_observer import constants as c

GREEN = ('\033[92m')    #green
YELLOW = ('\033[93m')   #yellow
RED = ('\033[91m')      #red
END = ('\033[0m')       #reset

key = input("API Key: ")

w = RiotObserver(key=key, default_region=c.EUROPE_WEST)

def wait():
    while not w.can_make_request():
        time.sleep(1)

try:
    print(YELLOW + "\nTesting: Summoner API" + END)
    s_name = input("> Summoner: ")
    s = w.get_summoner_by_name(summoner_name=s_name)
    wait()
    s_id = s['id']
    s_accid = s['accountId']
    print("> Summoner id: %s " % s_id)
    print("> Account id: %s " % s_accid)
    s = w.get_summoner_by_id(summoner_id=s_id)
    wait()
    s = w.get_summoner_by_accountid(account_id=s_accid)
    wait()
    print("> Name: %s " % s['name'])
    print(GREEN + "Summoner API is OK.\n" + END)
    time.sleep(2)

except LoLException as e:
    print(RED + "Error: %s" % e + "\n" + END)
    time.sleep(2)

input("Press enter to continue...")
time.sleep(2)

try:
    print(YELLOW + "\nTesting: Champion API" + END)
    c = w.get_all_champions(free_to_play=True)
    wait()
    c_id = c['champions'][0]['id']
    print("> Test id: %s " % c_id)
    c = w.get_champion(champion_id=c_id)
    wait()
    print("> Free to play: %s " % c['freeToPlay'])
    print(GREEN + "Champion API is OK.\n" + END)
    time.sleep(2)

except LoLException as e:
    print(RED + "Error: %s" % e + "\n" + END)
    time.sleep(2)

input("Press enter to continue...")
time.sleep(2)

try:
    print(YELLOW + "\nTesting: Spectator API" + END)
    g = w.get_featured_games()
    wait()
    g_name = g['gameList'][0]['participants'][0]['summonerName']
    game_id = g['gameList'][0]['gameId']
    print("> Test Summoner Name: %s " % g_name)
    g_id = w.get_summoner_by_name(summoner_name=g_name)['id']
    wait()
    print("> Summoner ID: %s " % g_id)
    g = w.get_current_game(summoner_id=g_id)
    wait()
    print(GREEN + "Spectator API is OK.\n" + END)
    time.sleep(2)

except LoLException as e:
    print(RED + "Error: %s" % e + "\n" + END)
    time.sleep(2)

input("Press enter to continue...")
time.sleep(2)

try:
    print(YELLOW + "\nTesting: Match API" + END)
    print("> Account ID: %s " % s_accid)
    mr = w.get_recent_matchlist(account_id=s_accid)
    wait()
    m = w.get_matchlist(account_id=s_accid)
    wait()
    m_id = m['matches'][0]['gameId']
    print("> Match id: %s " % m_id)
    m = w.get_match(match_id=m_id)
    wait()
    m = w.get_timeline(match_id=m_id)
    wait()
    print(GREEN + "Match API is OK.\n" + END)
    time.sleep(2)

except LoLException as e:
    print(RED + "Error: %s" % e + "\n" + END)
    time.sleep(2)

input("Press enter to continue...")
time.sleep(2)

try:
    print(YELLOW + "\nTesting: League API" + END)
    l = w.get_challenger()
    wait()
    lcn = l['entries'][0]['playerOrTeamName']
    print("> Challenger summoner: %s " % lcn)
    l = w.get_position(summoner_id=s_id)
    wait()
    print(GREEN + "League API is OK.\n" + END)
    time.sleep(2)

except LoLException as e:
    print(RED + "Error: %s" % e + "\n" + END)
    time.sleep(2)

input("Press enter to continue...")
time.sleep(2)

try:
    print(YELLOW + "\nTesting: Status API" + END)
    status = w.get_shard_data()
    wait()
    host = status['hostname']
    status_g = status['services'][0]['status']
    print("> Hostname: %s " % host)
    print("> Game status: %s " % status_g)
    print(GREEN + "League API is OK.\n" + END)
    time.sleep(2)

except LoLException as e:
    print(RED + "Error: %s" % e + "\n" + END)
    time.sleep(2)

input("Press enter to continue...")
time.sleep(2)

try:
    print(YELLOW + "\nTesting: Static Data API" + END)
    icons = w.static_get_icons()
    languages = w.static_get_languages()
    print("> Version: %s " % icons['version'])
    print(GREEN + "Static Data API is OK.\n" + END)
    time.sleep(2)

except LoLException as e:
    print(RED + "Error: %s" % e + "\n" + END)
    time.sleep(2)
