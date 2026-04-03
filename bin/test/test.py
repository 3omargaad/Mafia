class Thingy:
    def __init__(self):
        self.attribute = "Strange"

    def change(self):
        self.attribute = "Normal"


thing = Thingy()
thing.change()
print(thing.attribute)
thing.__init__()
print(thing.attribute)
