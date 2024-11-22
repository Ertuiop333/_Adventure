class X():
    def __init__(self):
        self.count = 5
        self.y = Y(self) #create a y passing in the current instance of x
    def add2(self):
        self.count += 2

class Y(X):
    def __init__(self,parent):
        self.parent = parent #set the parent attribute to a reference to the X which has it
        self.x = X()
    def modify(self):
        self.parent.add2()


x = X()
x.y.modify()
print(x.count)