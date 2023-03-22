class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self,value):
        first_node=Node(value)
        self.top=first_node
        self.height=1

    def print_list(self):
        temp=self.top
        while temp:
            print(temp.value,"->",end="")
            temp=temp.next

    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        self.height+=1

    def pop(self):
        popped_node=self.top
        self.top=self.top.next
        popped_node.next=None
        self.height-=1
        return popped_node.value 

    def is_empty(self):
        if self.height==0:
            print("\nIts empty")   
        else:
            print("\n Stack has values")
            self.print_list()


mystack=Stack(10)
mystack.push(23) 
mystack.push(24) 
mystack.push(25) 
mystack.print_list()  
x=mystack.pop()
print("\npopped Node:",x)
mystack.print_list() 
mystack.is_empty() 


