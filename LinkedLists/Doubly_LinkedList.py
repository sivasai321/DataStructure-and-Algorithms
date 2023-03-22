class double_Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class linkedlist:
   def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

   def printlist(self):
       if self.length==0:
         print("List is empty")
       else:
        temp=self.head
        while temp is not None:
            print(temp.value,"<=> ",end="")
            temp=temp.next

   def append(self,value) :
      new_node=double_Node(value)
      if self.length==0:
        self.head=new_node
        self.tail=new_node
      else:
        self.tail.next=new_node
        new_node.prev=self.tail
        self.tail=new_node
      self.length +=1

   def pop(self)   :
    if self.length==0:
     return None 
    temp=self.tail 
    if self.length==1:
        self.head=None
        self.tail=None
    else: 
      self.tail=self.tail.prev
      self.tail.next=None
      temp.prev=None
    self.length -=1
    return temp  
   
   def prepend(self,value):
    new_node=double_Node(value)
    if self.length==0:
        self.head=new_node
        self.tail=new_node
    else:
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

   def pop_first(self):
    if self.length==0:
        return None
    temp=self.head    
    if self.length==1:
        self.head=None
        self.tail=None
    else:
       self.head=temp.next
       self.head.prev=None
       temp.next=None
    self.length -=1
    return temp
   
   def add_before(self,target,value):
     if self.length==0:
        return None
     if self.head.value==target:  
        self.prepend(value)
        return True
     temp=self.head
     new_node=double_Node(value)
    
     while temp is not None:
        if temp.next.value==target:
            new_node.next=temp.next
            new_node.prev=temp
            temp.next.prev=new_node
            temp.next=new_node
            self.length +=1
            return True
        temp=temp.next    
     return False

   def reverseprint(self):
       if self.length==0:
         return None
       else:
        temp=self.tail
        while temp is not None:
            print(temp.value,"<=> ",end="")
            temp=temp.prev
  





dl1=linkedlist()
dl1.append(12)     
dl1.append(13)  
dl1.append(14)   
dl1.append(15)
dl1.printlist()
# x=dl1.pop()
# print("\nafter pop:")
# dl1.printlist()
# print("\npopped value:",x.value)
# dl1.prepend(11)   
# print("\nAfter Prepend:")
# dl1.printlist()
# x1=dl1.pop_first()
# print("\nAFter first pop:",x1.value)
print("\n")
dl1.reverseprint()

