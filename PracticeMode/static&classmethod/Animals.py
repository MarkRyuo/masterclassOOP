from abc import ABC, abstractmethod



# Todo create animal system can calculate the age of dog base in birth 
# Todo kailangan mabilang ang mga hayup na nakalagay sa system 



class Animal(ABC) :


    num_of_animals = 0

    def __init__(self, animalName: str, animalType: str, animalAge: int ) :
        self.animalName = animalName # ? A public class  
        self.animalType = animalType # ? A public class 
        self.animalAge = animalAge # ? A public class
    
    @abstractmethod  # * Create abstract method for passing in method talk() in the animals
    def talk(self) :
        pass  
    


    
