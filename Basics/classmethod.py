
class Marksman :
    
    def __init__(self, damage, hp) :
        self.damage = damage 
        self.hp = hp 


    def call(self) :
        print(
            f"Damage: {self.damage}
            )