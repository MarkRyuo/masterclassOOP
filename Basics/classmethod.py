



class Marksman :
    
    def __init__(self, damage: int, hp: int) : # ? Constructor 
        self.damage = damage # ? public Attribute 
        self.hp = hp # ? public Attribute


    # ? Method or function 
    def call(self) :
        print(f"Damage: {self.damage}")
        print(f"Hp: {self.hp}")
    

    @classmethod # ? This is a decorator (Most of the time class method is to provide alternati