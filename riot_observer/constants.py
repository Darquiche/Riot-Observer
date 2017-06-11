# REGIONS
RUSSIA = 'ru'
KOREA = 'kr'
BRAZIL = 'br1'
OCEANIA = 'oc1'
JAPAN = 'jp1'
NORTH_AMERICA = 'na1'
EUROPE_NORDIC_EAST = 'eun1'
EUROPE_WEST = 'euw1'
TURKEY = 'tr1'
LATIN_AMERICA_NORTH = 'la1'
LATIN_AMERICA_SOUTH = 'la2'

# SEASONS
seasons_id = {
    'PRESEASON3': 0,
    'SEASON3': 1,
    'PRESEASON2014': 2,
    'SEASON2014': 3,
    'PRESEASON2015': 4,
    'SEASON2015': 5,
    'PRESEASON2016': 6,
    'SEASON2016': 7,
    'PRESEASON2017': 8,
}

# MATCHMAKING QUEUES
queue_types = {
    'CUSTOM': 0,
    'NORMAL_3x3': 8,
    'NORMAL_5x5_BLIND': 2,
    'NORMAL_5x5_DRAFT': 14,
    'RANKED_SOLO_5x5': 4,
    'RANKED_FLEX_TT': 9,
    'RANKED_TEAM_5x5': 42,
    'ODIN_5x5_BLIND': 16,
    'ODIN_5x5_DRAFT': 17,
    'BOT_ODIN_5x5': 25,
    'BOT_5x5_INTRO': 31,
    'BOT_5x5_BEGINNER': 32,
    'BOT_5x5_INTERMEDIATE': 33,
    'BOT_TT_3x3': 52,
    'GROUP_FINDER_5x5': 61,
    'ARAM_5x5': 65,
    'ONEFORALL_5x5': 70,
    'FIRSTBLOOD_1x1': 72,
    'FIRSTBLOOD_2x2': 73,
    'SR_6x6': 75,
    'URF_5x5': 76,
    'ONEFORALL_MIRRORMODE_5x5': 78,
    'BOT_URF_5x5': 83,
    'NIGHTMARE_BOT_5x5_RANK1': 91,
    'NIGHTMARE_BOT_5x5_RANK2': 92,
    'NIGHTMARE_BOT_5x5_RANK5': 93,
    'ASCENSION_5x5': 96,
    'HEXAKILL': 98,
    'BILGEWATER_ARAM_5x5': 100,
    'KING_PORO_5x5': 300,
    'COUNTER_PICK': 310,
    'BILGEWATER_5x5': 313,
    'SIEGE': 315,
    'DEFINITELY_NOT_DOMINION_5x5': 317,
    'ARURF_5X5': 318,
    'ARSR_5x5': 325,
    'TEAM_BUILDER_DRAFT_UNRANKED_5x5': 400,
    'TEAM_BUILDER_RANKED_SOLO': 420,
    'TB_BLIND_SUMMONERS_RIFT_5x5': 430,
    'RANKED_FLEX_SR': 440,
    'ASSASSINATE_5x5': 600,
    'DARKSTAR_3x3': 610
}

# MAP NAMES
game_maps = [
    {'map_id': 1, 'name': "Summoner's Rift", 'notes': "Summer Variant"},
    {'map_id': 2, 'name': "Summoner's Rift", 'notes': "Autumn Variant"},
    {'map_id': 3, 'name': "The Proving Grounds", 'notes': "Tutorial Map"},
    {'map_id': 4, 'name': "Twisted Treeline", 'notes': "Original Version"},
    {'map_id': 8, 'name': "The Crystal Scar", 'notes': "Dominion Map"},
    {'map_id': 10, 'name': "Twisted Treeline", 'notes': "Current Version"},
    {'map_id': 11, 'name': "Summoner's Rift", 'notes': "Current Version"},
    {'map_id': 12, 'name': "Howling Abyss", 'notes': "ARAM Map"},
    {'map_id': 14, 'name': "Butcher's Bridge", 'notes': "ARAM Map"},
    {'map_id': 16, 'name': "Cosmic Ruins", 'notes': "Dark Star Map"},
]

# GAME/MATCH MODES
game_modes = [
    'CLASSIC',  # Classic Summoner's Rift and Twisted Treeline games
    'ODIN',  # Dominion/Crystal Scar games
    'ARAM',  # ARAM games
    'TUTORIAL',  # Tutorial games
    'ONEFORALL',  # One for All games
    'ASCENSION',  # Ascension games
    'FIRSTBLOOD',  # Snowdown Showdown games
    'KINGPORO',  # King Poro games
    'SIEGE',  # Nexus Siege games
    'ASSASSINATE',  # Blood Hunt Assassin games
    'ARSR',  # All Random Summoner's Rift games
    'DARKSTAR',  # Dark Star games
]

# GAME/MATCH TYPES
game_types = [
    'CUSTOM_GAME',  # Custom games
    'TUTORIAL_GAME',  # Tutorial games
    'MATCHED_GAME',  # All other games
]

# SUB TYPES
sub_types = [
    'NONE',  # Custom games
    'NORMAL',  # Summoner's Rift unranked games
    'NORMAL_3x3',  # Twisted Treeline unranked games
    'ODIN_UNRANKED',  # Dominion/Crystal Scar games
    'ARAM_UNRANKED_5v5',  # ARAM / Howling Abyss games
    'BOT',  # Summoner's Rift and Crystal Scar games played against AI
    'BOT_3x3',  # Twisted Treeline games played against AI
    'RANKED_SOLO_5x5',  # Summoner's Rift ranked solo queue games
    'RANKED_TEAM_3x3',  # Twisted Treeline ranked team games
    'RANKED_TEAM_5x5',  # Summoner's Rift ranked team games
    'ONEFORALL_5x5',  # One for All games
    'FIRSTBLOOD_1x1',  # Snowdown Showdown 1x1 games
    'FIRSTBLOOD_2x2',  # Snowdown Showdown 2x2 games
    'SR_6x6',  # Hexakill games
    'CAP_5x5',  # Team Builder games
    'URF',  # Ultra Rapid Fire games
    'URF_BOT',  # Ultra Rapid Fire games against AI
    'NIGHTMARE_BOT',  # Nightmare bots
    'ASCENSION',  # Ascension games
    'HEXAKILL',  # Twisted Treeline 6x6 Hexakill
    'KING_PORO',  # King Poro games
    'COUNTER_PICK',  # Nemesis games
    'BILGEWATER',  # Black Market Brawlers games
    'SIEGE',  # Nexus Siege games
    'RANKED_FLEX_TT',  # Ranked Flex Twisted Treeline games
    'RANKED_FLEX_SR',  # Ranked Flex Summoner's Rift games
    'DARKSTAR',  # Dark Star games
]

ranked_solo = 'RANKED_SOLO_5x5'
ranked_flex_sr = 'RANKED_FLEX_SR'
ranked_flex_tt = 'RANKED_FLEX_TT'
