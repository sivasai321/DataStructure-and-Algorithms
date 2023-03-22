class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:   
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.length ==0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail == None
        return temp 

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _  in range(index):
            temp = temp.next
        return temp.value

    def add_before(self,value,x):
        temp = self.head
        if temp.value == x:
            self.prepend(value)
            self.length +=1
            return True
        while temp.next is not None:
            if temp.next.value == x:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                self.length +=1
                return True
            temp = temp.next
        return None

    def add_after(self,value,x):
        if self.tail.value == x:
            self.append(value)
            self.length +=1
        temp = self.head
        while temp is not None:
            if temp.value == x:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                self.length +=1
                return True
            temp=temp.next
        return None

    def remove (self,x):
        if self.tail.value == x:
            self.pop()
        if self.head.value == x:
            self.pop_first()
        temp = self.head
        while temp.next is not None:
            if temp.next.value == x:
                removing_node = temp.next
                temp.next = temp.next.next
                removing_node.next= None
            temp=temp.next
        self.length -=1
        if self.length==0:
            self.head=None
            self.tail=None
        return removing_node
                
    def reverse(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp=after









my_linked_list = linkedList(5)

my_linked_list.prepend(20)
my_linked_list.append(30)
my_linked_list.add_before(30, 30)
my_linked_list.add_before(40, 5)
my_linked_list.add_before(100, 5)
my_linked_list.add_after(200, 20)
# print("deleted",my_linked_list.remove(100).value)



my_linked_list.print_list()
print("\n")
my_linked_list.reverse()
my_linked_list.print_list()