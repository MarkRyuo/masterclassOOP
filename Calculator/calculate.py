


class Calculate() :

    def __init__(self) -> None :
        pass
    
    def Get_Num1(self) :
        # * Enter a Number for NUM1
        # * If NUM1 is True return the value
        # * If NUM1 is false return False

        NUM1 = input("Enter a Number: ") # ? NUM1 is a constant 
        if int(NUM1) <= 10 :
            return False
        else :
            return True


    def Get_Num2(self)  :
        # * Enter a Number for NUM2
        # * If NUM2 is lessthan or equal to 10, return False 
        # * If NUM2 is greater than 10, return the value 

        NUM2 = input("Enter a Number: ")

        if int(NUM2) <= 10 :
            return False 
        else : 
            return True
    




