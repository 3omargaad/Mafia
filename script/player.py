import game_setup


class Player:
    def __init__(self, name, role, team, is_alive, audio_file, votes):
        self.name = name
        self.role = role
        self.team = team
        self.is_alive = is_alive
        self.audio_file = audio_file
        self.votes = votes
    # Initialises Default Attributes such as name, role, team, isAlive etc.

    def die(self):
        self.isAlive = False
    # Eliminates the player

    def heal(self):
        if self.isAlive is False:
            self.isAlive = True
    # Saves the player who has been aliminates

    def reveal_team(self):
        print(self.name + " is " + self.team)
    # Reveals the team which the player is in

    def reveal_role(self):
        print(self.name + " is " + self.role)
    # Reveals the role which the player has (not in use)

    def final_reveal(self):
        status = "Dead"
        if self.isAlive:
            status = "Alive"

        print(self.name + " is " + self.role + " (" + status + ")")

    def add_vote(self):
        self.votes += 1
    # Adds a vote onto the player

    def reset_vote(self):
        self.votes = 0
    # Removes all the player's votes

    # def sayName(self):
    #     newAudio = audio.convertToWav(inputFile=self.audioFile,
    #                   newName=self.name + ".wav")
    #     audio.playAudio(audio.newAudio)

# Player Object

# plrObject = player.Player(
#             name=plrName,
#             role="Civilian",
#             team="Good",
#             is_alive=True,
#             audio_file=None,
#             votes=0
# )
# DEFAULT SETTINGS FOR PLAYEROBJECT


def clear_player_list():
    game_setup.players.clear()
    game_setup.living_players.clear()


def create_player(plr_name):
    plr_object = Player(
        name=plr_name,
        role="Civilian",
        team="Good",
        is_alive=True,
        audio_file=None,
        votes=0
    )

    # Creates player object with default attributes

    game_setup.players.append(plr_object)
    game_setup.living_players.append(plr_object)
    # Adds player object to relevent arrays
