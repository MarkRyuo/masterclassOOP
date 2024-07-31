class Fighter:  # ? Blueprint

    def __init__(self, healthPoints):  # ? This is the constructor
        self.healthPoints = healthPoints
        # self.underAttack = underAttack

    def get_Hp(self):
        # todo create a logic here: if hero hp is lower than to 20 alert the player

        if self.healthPoints >= 100:
            self.healthPoints -= 20
            print(f"Your health is {self.healthPoints} your under attack")

        if self.healthPoints <= 20:
            print("Back up your health is low")


def main():

    fighterOne = Fighter(150)  # ? This is called intances
    # fighterOne.get_Hp()  # * 1st
    # fighterOne.get_Hp()  # * 2nd
    # fighterOne.get_Hp()  # * 3rd

    for x in range(4) :
        fighterOne.get_Hp()


main()
