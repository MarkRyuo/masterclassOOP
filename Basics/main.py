from typing import Self 


# Todo create a Person class 
# todo create a calculator class 


class Person :

    numberofPerson = 0 

    def __init__(self, nickname: str, gpa: int) -> None :
        self.nickname = nickname # ? public class 
        self.gpa = gpa # ? public class
    
    #* Instance Method
    def get_person_info(self) :
        return 