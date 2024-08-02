
class Marksman :
    
    def __init__(self, damage, hp) : # ? Constructor 
        self.damage = damage # ? public Attribute 
        self.hp = hp # ? public Attribute


    # ? Method or function 
    def call(self) :
        print(f"Damage: {self.damage}")
        print(f"Hp: {self.hp}")
    

    @classmethod # ? This is a decorator (Most of the time class method is to provide alternative to the init method)
    def clsmethod(cls) :
        print("I'm class method")



def main() :

    mm = Marksman(damage=400, hp=1000) #? This is good for practices    
    mm.call()

    mm.clsmethod()

main()


