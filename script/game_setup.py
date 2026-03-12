plr_num = 4  # Number of players
maf_num = 1  # Number of mafia
discussion_time = 30  # Discussion time
include_doc = False  # Whether the game has a Doctor
include_det = False  # Whether the game has a Doctor
anonymous_voting = False  # Whether the game has anonymous voting
allow_skip = False  # Whether the game has anonymous voting
execute_if_tie = False  # Whether the game has anonymous voting
host_name = "ChadGPT"  # Default host name
host_accent = "uk"  # Default host accent

players = []  # List of players in game
living_players = []  # List of living players in game
skip_vote = 0  # Amount of people voting skip (if applicable)
good_team_num = 3  # Default number of good team members
bad_team_num = 1  # Default number of bad team members
winnning_team = ""  # Final winning team

# Global variables for the game
# These need to be accessed by app.py and game_stages.py
