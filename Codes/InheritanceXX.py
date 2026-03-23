class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
        

    def fun(self):
        print("Inside fun method of parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructor")
        

    def fun(self):
        super().fun()
        print("Inside fun method of Child")    

cobj = Child()

cobj.fun()
