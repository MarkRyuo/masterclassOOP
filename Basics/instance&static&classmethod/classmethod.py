from typing import Self
from datetime import date 


class Person :

    def __init__(self, name: str, age: int ) :
        self.name = name 
        self.age = age 
    
    def description(self) :
        return f"{self.name} is {self.age} years old"




