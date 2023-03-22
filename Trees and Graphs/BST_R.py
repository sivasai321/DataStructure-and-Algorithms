class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None


    def recursive_contains(self,curr_node,value):
        if curr_node==None:
            return False
        if value==curr_node.value: 
            return True
        if value<curr_node.value:
            return self.recursive_contains(curr_node.left,value)
        if value>curr_node.value:
             return self.recursive_contains(curr_node.right,value)

    def r_contains(self,value):
        return self.recursive_contains(self.root,value)
    
    def recursive_insert(self,curr_node,value):
        if curr_node==None:
            return Node(value)
        if value<curr_node.value:
            curr_node.left=self.recursive_insert(curr_node.left,value)
        if value>curr_node.value:
            curr_node.right=self.recursive_insert(curr_node.right,value)    
        return curr_node

    def r_insert(self,value):
        if self.root==None:
            self.root=Node(value) 
        self.recursive_insert(self.root,value)     

    def delete_node(self,current_node,value):
        if current_node==None:
            return None
        if value<current_node.value:
            current_node.left=self.delete_node(current_node.left,value)
        
        if value>current_node.value:
            current_node.right=self.delete_node(current_node.right,value)
        return current_node    

    def d_node(self,value):
        self.delete_node(self.root,value)

myTree=BinarySearchTree()                             
myTree.r_insert(2)
myTree.r_insert(1)
myTree.r_insert(3)
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
print(myTree.r_contains(3))
print(myTree.r_contains(18))