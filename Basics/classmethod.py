
class Marksman :
    
    def __init__(self, damage, hp) : # ? Constructor 
        self.damage = damage # ? public Attribute 
        self.hp = hp # ? public Attribute


    # ? Method or function 
    def call(self) :
        print(f"Damage: {self.damage}")
        print(f"Hp: {self.hp}")
    

    @classmethod # ? This is a decorator 
    def 