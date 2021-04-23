import rng
import random

class EnemySettings:
    MAX_ATTACK_THRESHOLD = 256

class Enemy():
    def __init__(self, tags):
        self.tags = tags
        self.rngObj = rng.PRNG(a=random.randint(1,100), b=random.randint(1,100), c=random.randint(1,100))

        # TAG DATA
        self.canAttack = self.tags['canAttack']
        self.damageMax = self.tags['damageMax']
        self.damageMin = self.tags['damageMin']
        self.health = self.tags['health']

    def get_random_number(self):
        self.rngObj._change(a=random.randint(1,100), b=random.randint(1,100), c=random.randint(1,100))
        res = self.rngObj._gen(res='int', max_size=30)

        return res

    
    def attack(self):
        if self.canAttack == False:
            print("[Debug]: attack() cannot start if canAttack is False!")
        else:
            shouldAttack = self.get_random_number()
            #print(shouldAttack)
            if shouldAttack > EnemySettings.MAX_ATTACK_THRESHOLD:
                print("attack!")
                pass
            else:
                print("dont attack!")
                pass

while True:
    tags = {
        'canAttack': True,
        'damageMax': 30,
        'damageMin': 20,
        'health': 30
    }
    e = Enemy(tags=tags)
    e.attack()