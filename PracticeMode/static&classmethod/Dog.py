from Animals import Animal


class Dog(Animal) :

    def __init__(self, animalName: str, animalType: str, dateofbirth: int) :
        super().__init__(animalName, animalType, dateofbirth) #* Importing the super class 
    

