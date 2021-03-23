

#self is the self-reference in a Class. Your code is not in a class, you only have functions defined. You have to wrap your methods in a class, like below. To use the method main(), you first have to instantiate an object of your class and call the function on the object.

#Further, your function setavalue should be in __init___, the method called when instantiating an object. The next step you probably should look at is supplying the name as an argument to init, so you can create arbitrarily named objects of the Name class ;)

class Name:
    def __init__(self):
        self.myname = "harry"

    def printaname(self):
        print ("Name", self.myname)     

    def main(self):
        self.printaname()

if __name__ == "__main__":
    objName = Name()
    objName.main() 
