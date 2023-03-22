class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def add(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

        self.length +=1


    def printList(self):
        if self.length==0:
            return None
        temp=self.head
        while temp:
            print(temp.value,"->",end="")
            temp=temp.next



mylist=LinkedList()
mylist.add(1)
mylist.add(2)
mylist.printList()




                            