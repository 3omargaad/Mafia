class Player:
    def __init__(self, name, role, team, isAlive, audioFile, votes):
        self.name = name
        self.role = role
        self.team = team
        self.isAlive = isAlive
        self.audioFile = audioFile
        self.votes = votes

    def die(self):
        self.isAlive = False

    def heal(self):
        if self.isAlive == False:
            self.isAlive = True

    def revealTeam(self):
        print(self.name + " is " + self.team)

    def revealRole(self):
        print(self.name + " is " + self.role)
    
    def finalReveal(self):
        status = "Dead"
        if self.isAlive:
            status = "Alive"

        print(self.name + " is " + self.role + " (" + status + ")")
        
    def addVote(self):
        self.votes += 1

    def resetVote(self):
        self.votes = 0

    #def sayName(self):
    #    newAudio = audio.convertToWav(inputFile=self.audioFile, newName=self.name + ".wav")
    #    audio.playAudio(audio.newAudio)

# Player Object

#plrObject = player.Player(name=plrName, role="Civilian", team="Good", isAlive=True, audioFile=None, votes=0)
# DEFAULT SETTINGS FOR PLAYEROBJECT