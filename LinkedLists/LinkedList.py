class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0


    def insert(self,value):
        new_node=Node(value)
        if self.length==0:
             self.head=new_node
             self.tail=new_node
        else:
            self.tail.next=new_node     
            self.tail= new_node
        self.length +=1

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        before=None
        after=temp.next
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
        return True    
     

    def converttoarray(self):
        array=[]
        temp=self.head    
        while temp:
                array.append(temp.value)
                temp=temp.next
        return array


    def printlist(self):
     if self.length==0:
        print("list is empty")
     else:
        temp=self.head
        while temp is not None:
            print(temp.value,"=>",end="")
            temp=temp.next



l1=linkedlist()
l1.insert(1)
l1.insert(12)
l1.insert(31)
l1.insert(41)
l1.insert(11)
l1.printlist()
# res=l1.converttoarray()
# print("\n")
# print(res)
print("\n")
l1.reverse()
l1.printlist()

