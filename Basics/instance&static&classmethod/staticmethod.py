


class Person :

    def __init__(self, name: str, age: int) :
        self.name = name 
        self.age = age 
    
    def description(self) :
        return f"{self.name} is {self.age} years old!"
    
    @staticmethod
    def add_numbers(*numbers: float) -> float:
        return sum(numbers)


if __name__ == '__main__' :
    p1 = Person("moda", 21)
    
