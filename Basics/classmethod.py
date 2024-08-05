



class Marksman :
    
    def __init__(self, damage: int, hp: int) : # ? Constructor 
        self.damage = damage # ? public Attribute 
        self.hp = hp # ? public Attribute


    # ? Method or function 
    def call(self) :
        print(f"Damage: {self.damage}")
        print(f"Hp: {self.hp}")
    

    @classmethod 
    def clsmethod(cls) :
        print("I'm class method")



def main() :

    mm = Marksman(damage=400, hp=1000) #? This is good for practices    
    mm.call()
