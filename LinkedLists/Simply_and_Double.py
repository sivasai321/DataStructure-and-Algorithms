class Single_Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Double_Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

#to insert into a linked list
    def insert2single(self,value):
        new_node=Single_Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1    

# to insert into doubly linked list
    def insert2doubly(self,value):
      new_node=Double_Node(value)
      if self.length==0:
        self.head=new_node
        self.tail=new_node
      else:  
        self.tail.next=new_node
        new_node.prev=self.tail
        self.tail=new_node
      self.length +=1   

#to insert into beginning of L
    def add2begin_single(self,value):
        new_node=Single_Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:    
            temp=self.head
            self.head=new_node
            self.head.next=temp
        self.length +=1    
    
    def add2begin_double(self,value):
        new_node=Double_Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            temp=self.head
            self.head=new_node
            self.head.next=temp
            temp.prev=new_node
        self.length +=1        
  
    def specificdelete_single(self,x):
        if self.length==0:
            return None
        temp=self.head
        while temp.next is not None:
            if temp.next.value==x:
                flag=temp.next
                temp.next=temp.next.next
                flag.next=None
                self.length -=1
            temp=temp.next

    def specificdelete_double(self,x):
        if self.length==0:
            return None
        temp=self.head
        while temp.next is not None:
            if temp.next.value==x:
              flag=temp.next
              temp.next=temp.next.next
              flag.next.prev=temp
              flag.next=None
              flag.prev=None
              self.length -=1
              return None
            temp=temp.next  

    def insertafter_single(self,value,x):
        if self.length==0:
            return None
        if self.tail.value==x:
            self.insert2single(value)    
            return True
        temp=self.head
        while temp.next is not None:
            if temp.value==x:
               new_node=Single_Node(value)
               new_node.next=temp.next
               temp.next=new_node
               self.length +=1
               return True
            temp=temp.next   
        return False

    def insertafter_double(self,value,x):
        if self.length==0:
            return None
        if self.tail==x   :
            pass    


        
                  
                  # printing functions #
                #------------------------#

    def printlist_single(self):    #same Logic for both the lists
        if self.length==0:
            return None
        temp=self.head
        while temp is not None:
            print(temp.value,"-> ",end="")    
            temp=temp.next

    def printlist_double(self):    
        if self.length==0:
            return None
        temp=self.head
        while temp is not None:
            print(temp.value,"<=> ",end="")    
            temp=temp.next


mylist=LinkedList()
mylistD=LinkedList() # for doubley linked

# add commands via mylist.function_name()

mylist.insert2single(1)
mylist.insert2single(2)
mylist.insert2single(3)
mylist.insert2single(4)
mylist.insert2single(5)
mylist.add2begin_single(0)
# mylist.specificdelete_single(3)
mylist.insertafter_single(6,4)



mylistD.insert2doubly(10)
mylistD.insert2doubly(20)
mylistD.insert2doubly(30)
mylistD.insert2doubly(40)
mylistD.insert2doubly(50)
mylistD.add2begin_double(9)
# mylistD.specificdelete_double(30)


print("After Insert") 
mylist.printlist_single()
print("\n")
mylistD.printlist_double()

