import moduleOne # ? Import the moduleOne

# ? In order to prevent code an import to be executed when it is imported we have to add a guard is the guard is if __name__ == '__main__' : statement 

def main() :
    moduleOne.call("moda")


if __name__ == '__main__' : # ? This is like a guard
    main()
    print("Main is running....")