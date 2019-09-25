class Monster():
    def __init__(self, name, eyes, fur, list, height):
        self.name = name
        self.number_eyes = int(eyes)
        self.fur_type = fur
        self.skills = list
        self.cuteness = 0
        self.height = int(height)
    def scare(self):
        return 'GURRRRRRRRRRRR'
    def eat(self):
        return 'GUmp GUMP GUMP GUMP'
    def transforn(self):
        return 'beeeep beeeeep beeeeeeeeeeeeeeeeeeeeeeep'
    def run(self):
        return "Never, Monster's walk"
    def fart(self):
        return 'puitttttttttttt'
    def laugh(self):
        return 'HIGAGAGAGAG AGAGAGGAGAGA'