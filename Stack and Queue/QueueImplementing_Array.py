#Queue implemention using Lists/Array
import collections
class Queue:
    def __init__(self):
        self.items=[]

    def enque(self,value):
        self.items.append(value)    

    def deque(self):
        return self.items.pop(0)

    def Display(self):
        print(self.items)

    def isEmpty(self):
        if self.items==0:
            print("Empty Queue")
        else:
            print("Not empty")        

myQ=Queue()
myQ.enque(1)
myQ.enque(2)
myQ.enque(3)
myQ.enque(4)
myQ.Display()
x=myQ.deque()
print("\n Popped value:",x)
myQ.isEmpty()

myQ=collections.deque()    #the brackets are important
myQ.append(10)
myQ.append(102)
myQ.append(103)
print(myQ)
myQ.popleft()
print(myQ)