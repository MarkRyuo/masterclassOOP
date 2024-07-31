


class Fighter : # ? Blueprint 
    
    def __init__(self, healthPoints) : # ? This is the constructor 
        self.healthPoints = healthPoints
    
    def get_Hp(self) ;
        print(f"Hero Hp: {self.healthPoints}")


fighterOne = Fighter(1000) # ? This is called intances
