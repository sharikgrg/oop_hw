from monster_hw import *
# (self, name, eyes, fur, list, height)
monster = Monster('godzilla', 2, 'soft', ['crying', 'dying', 'lasers'], 800 )
print(monster.name)
print(monster.skills)
print(monster.scare())

monster1 = Monster('mojojojo', 100, 'sad', ['shouting', 'dying', 'inventing'], 10 )
print(monster1.name)
print(monster1.skills)
print(monster1.scare())

monster2 = Monster('doflamingo', 2, 'no fur', ['killing', 'manipulating', 'hello'], 800 )
print(monster2.name)
print(monster2.skills)
print(monster2.scare())