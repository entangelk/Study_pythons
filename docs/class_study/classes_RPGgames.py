# function만 사용해 적 케릭터 만들기
# first 적 캐릭터
'''
name = 'first'
health = 120
damage = 0


def attack(damage):
    health = health-damage
    return health

damage = attack(5)  # ???? health가 아니고?



# second 적 캐릭터
name = 'second'
health = 200
damage = 0

damage = attack(10)
'''
# function만 사용 시 제한 극복 -> class

class Enemy:
    def __init__(self,name,health): # 생성자
        self.name = name
        self.health = health
        self.damage = 0
        pass
    def attack(self, damage):
        self.health = self.health-damage
        return self.health
    

first_enemy = Enemy("enemy1",120)
second_enemy = Enemy("enemy2",200)
print(first_enemy.attack(5))
print(second_enemy.attack(20))