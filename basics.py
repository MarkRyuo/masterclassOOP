class Fighter:  # ? Blueprint

    def __init__(self, healthPoints):  # ? This is the constructor
        self.healthPoints = healthPoints

    def get_Hp(self):

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

    for x in range(5) :
        fighterOne.get_Hp()


main()
