from Animals import Animal


class Dog(Animal) :

    def __init__(self, animalName: str, animalType: str, dateofbirth: int) :
        super().__init__(animalName, animalType, dateofbirth) #* Importing the super class 
    

    def talk(self): 
        return f"{self.animalName} said Woof! Woof!"



    
if __name__ == '__main__' :
    print("This is Dog")
else :
    print("Dog! Running Outside")
