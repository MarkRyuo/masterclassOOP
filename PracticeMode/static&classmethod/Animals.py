from abc import ABC, abstractmethod



# Todo create animal system can calculate the age of dog base in birth 
# Todo kailangan mabilang ang mga hayup na nakalagay sa system 



class Animal(ABC) :


    num_of_animals: int = 0  # ? Type hints (:) make your code more readable

    def __init__(self, animalName: str, animalType: str, dateofbirth: int ) :
        self.animalName = animalName # ? A public class  
        self.animalType = animalType # ? A public class 
        self.dateofbirth = dateofbirth # ? A public class
        Animal.num_of_animals += 1 #* Increamenting animals if adding animal

    @abstractmethod  # * Create abstract method for passing in method talk() in the animals
    def talk(self) :
        pass

    @classmethod 
    def get_total_age(cls, dateofbirth: int, animalAge: int) -> int :
        return dateofbirth # ! Im not done yet
    

if __name__ == '__main__' :
    print("Main Animal Running")
else :
    print("Running Outside")
    
