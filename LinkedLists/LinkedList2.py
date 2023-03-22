class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class linkedlist:
   def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

   def printlist(self):
     if self.length==0:
        print("list is empty")
     else:
        temp=self.head
        while temp is not None:
            print(temp.value,"=>",end="")
            temp=temp.next

   def append(self,value):
        new_node=Node(value)
        if self.length==0:
             self.head=new_node
             self.tail=new_node
        else:
            self.tail.next=new_node     
            self.tail= new_node
        self.length +=1

   def pop(self):
    if self.length==0:
        return None
    temp=self.head    
    prev=self.head    
    if self.length==1:
        self.head=None
        self.tail=None
    else:
 
        while temp.next is not None:
            prev=temp
            temp=temp.next
        prev.next=None
        self.tail=prev    
    self.length -=1 
    return temp  

   def prepend(self,value):
    new_node=Node(value)
    if self.length==0:
        self.head=new_node
        self.tail=new_node
    else:
        new_node.next=self.head
        self.head=new_node
    self.length +=1
    return True

   def pop_first(self):
    if self.length==0:
        return None
    temp=self.head    
    if self.length==1:
        self.head=None
        self.tail=None
    else:
       self.head=temp.next
       temp.next=None
    self.length -=1
    return temp

   def get_value(self,target): 
        if self.length==0:
            print("empty list")
        else:
          temp=self.head
          while temp is not None:
            if temp.value==target:
                print("value found")
                return True
            temp=temp.next
        print("Value not found")    

   def get_index(self,index):
     if self.length==0:
            print("empty list")
            return True
     if self.length>index and  0 <=index :
        print("Index exists")
        temp=self.head
        count=0
        while temp is not None:
            if index==count:
                print("Index value:",temp.value)
                return True
            else:
                temp=temp.next
                count +=1    
     else:
        print("index does not exist")       

   def add_before(self,target,value):
     if self.length==0:
        return None
     if self.head.value==target:
        self.prepend(value)
        return True
     new_node=Node(value)
     temp=self.head
     while temp.next is not None:
        if temp.next.value==target:
            new_node.next=temp.next
            temp.next=new_node
            return True
     self.length +=1
     return False


   def add_after(self,target,value):
    if self.length==0:
        return None
    if self.tail==target:
        self.append()
        return True
    new_node=Node(value)
    temp=self.head
    while temp.next is not None:
        if temp.value==target:
            new_node.next=temp.next
            temp.next=new_node
            self.length +=1
            return True
        temp=temp.next    
    return False
            
   def reverse(self):
    if self.length==0:
        return None
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
  


l1=linkedlist()
l1.append(100)
l1.append(101)
l1.append(103)
l1.append(104)

# x=l1.pop()
# print("after pop:")
# l1.printlist()
# print("popped value:",x.value)
l1.prepend(99)
# print("AFter prepend:")
# l1.printlist()
# x1=l1.pop_first()
# print("AFter first pop:",x1.value)
# l1.printlist()
# # l1.get_value(100)
# l1.get_index(3)


l1.add_before(99,122)

l1.printlist()
l1.reverse()
print("\n")

l1.printlist()
# l1.add_after(100,35)
# print("\n Add After")

# l1.printlist()







            
         