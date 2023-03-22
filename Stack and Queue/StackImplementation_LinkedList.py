class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,value):
        new_node=Node(value)    
        new_node.next=self.top
        self.top=new_node
        self.size =self.size+1

    def pop(self):
        if self.top is None:
            return None
        popped_node=self.top
        self.top=popped_node.next   
        self.size =self.size-1
        return popped_node.value

    def printstack(self):
        temp=self.top
        while temp:
            print(temp.value,"->",end="")
            temp=temp.next
    def isEmpty(self):
        if self.size==0:
            return -1

newstack=Stack()
newstack.push(1)
newstack.push(2)
newstack.push(3)
newstack.push(4)
newstack.push(5)
newstack.push(6)
newstack.printstack()
x=newstack.pop()
print("\nPopped Value:",x)
newstack.printstack()
r=newstack.isEmpty()
if r==-1:
    print("\nEmpty")
else:
    print("\nNot Empty")    
