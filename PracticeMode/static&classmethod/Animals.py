from abc import ABC, abstractmethod



# Todo create animal system can calculate the age of dog base in birth 




class Animal(ABC) :



    def __init__(self, animalName: str, animalType: str, animalAge: int ) :
        self.animalName = animalName # ? A public class  
        self.animalType = animalType
        self.animalAge = animalAge
    
