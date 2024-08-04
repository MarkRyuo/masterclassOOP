from typing import Self
from datetime import date 


# ? A class method is going to effect the actual class while an instance method is going to effect the instance 


class Person :

    def __init__(self, name: str, age: int ) :
        self.name = name 
        self.age = age 
    
    def description(self) :
        return f"{self.name} is {self.age} years old"


    @classmethod 

    def age_from_year(cls, name: str, birth_year: int) -> Self :
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)
    


if __name__ == '__main__' :

    moda = Person.age_from_year("moda", 2003)
    print(moda.description())





