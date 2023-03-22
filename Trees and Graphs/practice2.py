class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None        

    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while(True):
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left =new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right

    def DFS_PostOrder(self):
        results=[]
        def Traversal(curr_Node):
            if curr_Node.left is not None:
                Traversal(curr_Node.left)
            if curr_Node.right is not None:
                Traversal(curr_Node.right)
            results.append(curr_Node.value)  
        Traversal(self.root)    
        return results 

    def contains(self,value):
        temp=self.root
        while temp is not None:
            if value<temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False            
