


class Calculate() :

    def __init__(self) -> None :
        pass
    
    def Get_Number(self) :
        # * Enter a Num1 

        num1: int = input("Enter a NumA: ") # type: ignore
        if num1 <= 10 :
            return False
        else :
            return True



if __name__ == '__main__' :
    getNUm = Calculate()
    print(getNUm.Get_Number())
