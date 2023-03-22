class Node:
    def __init__(self,value):   # self is used in method inside a class whenever an instance is used to call itself like this keyword
        self.value=value
        self.next=None

class Linkedlist:
  def __init__(self):
     self.head=None
     self.tail: None
     self.length=0

  def print_linkedlist(self):
     temp=self.head
     while temp is not None:
        print(temp.value)
        temp=temp.next  

  def append(self,value):
    new_node=Node(value)
    if self.head is None:
        self.head=new_node
        self.tail=new_node
    else:    
        self.tail.next=new_node
        self.tail=new_node

    self.length +=1        
    return True

  def pop(self):
   if self.head == None:
    print ('empty list')  
   else:
    temp=self.head
    prev=self.head
    while temp.next is not None:
        prev=temp
        temp=temp.next

   self.tail=prev
   self.tail.next=None
   self.length -=1 
   if self.length==0:
        self.head=None
        self.tail=None

   return temp

  def prepend(self,value):
     new_node=Node(value)
     if self.head is None:  
        self.head=new_node
        self.tail=new_node
     else:
        new_node.next=self.head
        self.head=new_node 
            
     self.length +=1
     return True

  def pop_first(self):
    if self.head is None:
        return None
    else:
      temp=self.head
      self.head=self.head.next
      temp.next=None
    self.length -=1
    if self.length==0:
        self.head=None
        self.tail=None 
    return temp
    


mylist=Linkedlist()
mylist.append(1)
mylist.append(23)
mylist.append(53)

mylist.print_linkedlist()
popped = mylist.pop()
print("PV:",popped.value)
mylist.prepend(90)
mylist.print_linkedlist()
f_pop=mylist.pop_first()
print("First Pop:",f_pop.value)
