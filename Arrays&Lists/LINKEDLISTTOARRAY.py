# class Node:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

# def array_to_linked_list(arr):
#     dummy = Node()
#     curr = dummy
#     for val in arr:
#         curr.next = Node(val)
#         curr = curr.next
#     return dummy.next

# arr = [1, 2, 3, 4, 5]
# linked_list = array_to_linked_list(arr)
# while linked_list:
#     print(linked_list.val)
#     linked_list = linked_list.next


class Single_Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def appender(self,value):
        new_node=Single_Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length +=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length +=1

    def printlist_single(self):    #same Logic for both the lists
        if self.length==0:
            return None
        temp=self.head
        while temp is not None:
            print(temp.value,"-> ",end="")    

            temp=temp.next


arr=[1,2,3,4,5,6]
print(arr)
lister=Linkedlist()
for i in range(len(arr)):
    value=arr[i]
    lister.appender(value)

lister.printlist_single()    




