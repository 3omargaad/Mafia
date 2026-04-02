from random import choice

from player import Player


class Game:
    def __init__(self):
        self.plr_num = 4  # Number of players
        self.maf_num = 1  # Number of mafia
        self.discussion_time = 30  # Discussion time
        self.include_doc = False  # Whether the game has a Doctor
        self.include_det = False  # Whether the game has a Detective
        self.anonymous_voting = False  # Whether the game has anonymous voting
        self.allow_skip = False  # Whether the game has anonymous voting
        self.execute_if_tie = False  # Whether the game has anonymous voting
        self.host_name = "ChadGPT"  # Default host name
        self.host_accent = "uk"  # Default host accent
        self.game_stage = "Intro"  # The stage which the game is at
        self.vote_count = 0  # Player number who last voted

        self.players = []  # List of players in game
        self.votes = []  # List of player votes
        self.living_players = []  # List of living players in game
        self.dead_players = []  # List of dead players in game
        self.skip_vote = 0  # Amount of people voting skip (if applicable)
        self.good_team_num = 3  # Default number of good team members
        self.bad_team_num = 1  # Default number of bad team members
        self.winnning_team = ""  # Final winning team
    # Initialises Default Attributes such as name, role, team, isAlive etc.

    def create_player(self, plr_name):
        plr_object = Player(
            name=plr_name,
            role="Civilian",
            team="Good",
            is_alive=True,
            audio_file=None,
            votes=0
        )

        self.players.append(plr_object)
        self.living_players.append(plr_object)
        # Creates player object with default attributes

    def clear_player_list(self):
        self.players.clear()
        self.living_players.clear()

    def get_player(self, name: str):
        for plr in self.players:
            if getattr(plr, "name", None) == name:
                return plr
        raise ValueError(f"No player found with name={name!r}")

    def set_stage(self, stage):
        self.game_stage = stage

    def remove_dead_players(self):
        for plr in self.players:
            if plr.is_alive is False:
                self.living_players.remove(plr)
                self.dead_players.append(plr)
            # Removes dead players from list

    def reset_votes(self):
        self.vote_count = 0
        self.votes.clear()
        for plr in self.living_players:
            plr.reset_vote()

    def execute_voted_player(self, *args):
        for plr in self.living_players:
            self.votes.append(plr.votes)

        max_vote = max(self.votes)
        executed_players = []

        for plr in self.living_players:
            if plr.votes == max_vote:
                executed_players.append(plr)

        executed_player = choice(executed_players)
        executed_player.die()


game = Game()
