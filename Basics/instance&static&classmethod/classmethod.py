from typing import Self
from datetime import date 


# ? A class method is going to effect the actual class while an instance method is going to effect the instance 


class Person :

    def __init__(self, name: str, age: int ) :
        self.name = name 
        self.age = age 
    
    def description(self) :
        return f"{self.name} is {self.age} years old"


    @classmethod # ? This is a decorator (Most of the time class method is to provide alternative to the init method)
    def age_from_year(cls, name: str, birth_year: int) -> Self : # ? function annonation (->): this arrow is uses to Understand your code in function
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)
    

if __name__ == '__main__' :

    moda = Person.age_from_year("moda", 2003)
    print(moda.description())





