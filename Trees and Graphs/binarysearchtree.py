class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def Insert_Node(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node 
            return True
        temp=self.root
        while(True):
            if new_node.value==temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node    
                    return True
                temp=temp.right

    def contains(self,value):  
        temp=self.root
        while temp is not None:
            if value < temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False          

    def BFS(self):
        current_node=self.root
        queue=[]
        results=[]
        queue.append(current_node)
        while len(queue)>0:
            current_node=queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left) 
            if current_node.right is not None: 
                queue.append(current_node.right)  
        return results        

    def DFS_PreOrder(self):
        results=[]
        def Traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                Traverse(current_node.left)
            if current_node.right is not None:
                Traverse(current_node.right)    
        Traverse(self.root)
        return results
    
    def DFS_PostOrder(self):
        results=[]
        def traverse(current_node):    
            if current_node.left is not  None:
                traverse(current_node.left)

            if current_node.right is not None:
                traverse(current_node.right) 

            results.append(current_node.value)
        traverse(self.root)
        return results

    def DFS_InOrder(self):
        results=[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root) 
        return results           

myTree=BinarySearchTree()                             
myTree.Insert_Node(47)
myTree.Insert_Node(21)
myTree.Insert_Node(76)
myTree.Insert_Node(18)
myTree.Insert_Node(27)
myTree.Insert_Node(52)
myTree.Insert_Node(82)
print("BFS:")
print(myTree.BFS())
print("DFS Pre Order:")
print(myTree.DFS_PreOrder())
print("DFS Post Order:")
print(myTree.DFS_PostOrder())
print("DFS In Order:")
print(myTree.DFS_InOrder())
print(myTree.contains(11))
print(myTree.contains(1))