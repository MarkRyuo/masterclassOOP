

# ? Intance Method 


class Animal :

    def __init__(self, animalName: str , animalAge) :
        self.animalName = animalName
        self.animalAge = animalAge 
    
    def display(self) :
        return f"{self.animalName} is {self.animalAge} years old!"