#create a linked list and write a function to add node at begin

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def addbegin(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length +=1
        else:
            temp=self.head
            self.head=new_node
            self.head.next=temp
            self.length +=1

    def addvalues(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length +=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length +=1    

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.value,"->",end="")
            temp=temp.next           


l1=Linkedlist()
l1.addvalues(1)
l1.addvalues(21)
l1.addvalues(31)
l1.addvalues(41)

l1.printlist()
print("\n")
l1.addbegin(22)
l1.printlist()



