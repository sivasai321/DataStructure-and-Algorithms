#Stack Implementation using arrays
class Stack:
    def __init__(self):
        self.items=[]

    def push(self,value):
        self.items.append(value)  

    def pop(self):
        return self.items.pop()      

    def is_empty(self):
        return len(self.items)

    def printstack(self):
        print(self.items)
         

newstack=Stack()
newstack.push(10)
newstack.push(20)
newstack.push(30)
newstack.push(40)
newstack.push(50)
x=newstack.is_empty()
print(x)
newstack.printstack()
newstack.pop()
newstack.printstack()

