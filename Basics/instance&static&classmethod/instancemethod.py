

# ? Intance Method 


class Animal :

    def __init__(self, animalName: str , animalAge: int) :
        self.animalName = animalName
        self.animalAge = animalAge 
    
    def display(self) :
        return f"Pet name: {self.animalName} is {self.animalAge} years old!"




if __name__ == '__main__' :
    A1 = Animal("Rambo", 10)