class Node:
    def __init__(self,d):
        self.data=d
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def addtolist(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length +=1


        else:
            self.tail.next=new_node      
            new_node=self.tail
            self.length +=1

            

    def printlist(self):
        if self.length==0:
            return None
        temp=self.head
        while temp is not None:
            print(temp.data)   
            temp=temp.next


l1=linkedlist()
l1.addtolist(10)
l1.addtolist(20)
l1.addtolist(12)
l1.printlist()


