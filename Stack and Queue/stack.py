class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,value):
        newnode=Node(value)
        if self.size==0:
            self.top=newnode
            self.size+=1
        else:
            newnode.next=self.top
            self.top=newnode
            self.size+=1

    def pop(self):
        
        popped_node=self.top
        self.top=None
        self.size-=1
        return  popped_node
    
    def is_empty(self):
        if self.size==0:
            return -1
        

    def display(self):
        temp=self.top
        while temp is not None:
            print(temp.value,"->",end="")    
            temp=temp.next


mystack=Stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)
mystack.display()
x=mystack.is_empty()
if x==-1:
    print("\nStack is empty")
else:
    print("\nStack Has values")