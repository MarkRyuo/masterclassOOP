# from typing import Self 


# Todo create a Person class 
# todo create a calculator class 


class Person :

    numberofPerson = 0 

    def __init__(self, nickname: str, gpa: float) -> None :
        self.nickname = nickname # ? public class 
        self.gpa = gpa # ? public class
        Person.numberofPerson += 1 #* Bawat lagay, Increment by 1
    
    #? Instance Method
    def get_person_info(self) :
        return f"Nickname: {self.nickname} \nGpa: {self.gpa}"
    



if __name__ == '__main__' :
    # ? Instances
    p1 = Person("moda", 1.20)
    print(p1.get_person_info())

    print(Person.numberofPerson) # * Bawat lagay ng person dumadag-dag