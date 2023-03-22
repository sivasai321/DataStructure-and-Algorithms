class Graph:
    def __init__(self):
        self.adj_list={}

    def printGraph(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])    

    def addvertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[] 
            return True
        return False  
    
    
    def addedge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): #has to be in.. so dont use not in
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
