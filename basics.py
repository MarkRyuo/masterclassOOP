


class Fighter : # ? Blueprint 
    
    def __init__(self, healthPoints, underAttack) : # ? This is the constructor 
        self.healthPoints = healthPoints
        self.underAttack = underAttack
    
    def get_Hp(self) :
        # todo create a logic here: if hero hp is lower than  to 10 alert the player 
        if self.healthPoints > 1000 :
            self.healthPoints -= 150
            print(f"Your health is {self.healthPoints}")


fighterOne = Fighter(1000) # ? This is called intances
fighterOne.get_Hp()
