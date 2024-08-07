
# Todo create a Person class 
# todo create a calculator class 


class Person :

    numberofPerson = 0 
    courses = "BSIT"

    def __init__(self, nickname: str, gpa: float) -> None :
        self.nickname = nickname # ? public class 
        self.gpa = gpa # ? public class
        Person.numberofPerson += 1 #* Bawat lagay, Incremented by 1
    
    #? Instance Method
    def get_person_info(self) :
        return f"Nickname: {self.nickname} \nGpa: {self.gpa}"

    @classmethod
    def get_course(cls,) : # ? Can adopt the class 
        return f"Course: {cls.courses}"
    
    @staticmethod
    def calculate_Person(persons: int, number: int) -> int : # ? Cant adopt the class 
        return persons + number




if __name__ == '__main__' :
    # ? Instances
    p1 = Person(nickname="moda", gpa=1.20) #? Person 1 
    print(p1.get_person_info())

    print(f"person enrolled: {Person.numberofPerson}") # * Bawat lagay ng person dumadag-dag
    print(Person.get_course())

    print(Person.calculate_Person(2, 41111))