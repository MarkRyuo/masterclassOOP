from Animals import Animal


class Cat(Animal) :

    def __init__(self, animalName: str, animalType: str, dateofbirth: int) :
        super().__init__(animalName, animalType, dateofbirth) #* Importing the super class 
    

    def talk(self): 
        return f"{self.animalName} said Woof! Meow!"

    

    

