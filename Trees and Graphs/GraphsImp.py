class Graph:
    def __init__(self):
        self.adjacent_list={}

    def printGraph(self):
        for vertx in self.adjacent_list:
            print(vertx,':',self.adjacent_list[vertx])

    def AddVertex(self,vertex):
        if vertex not in self.adjacent_list.keys():
            self.adjacent_list[vertex]=[]    
            return True
        return False
    
    def Add_Edge(self,vertex1,vertex2):
        if vertex1 in self.adjacent_list.keys() and vertex2 in self.adjacent_list.keys():
            self.adjacent_list[vertex1].append(vertex2)
            self.adjacent_list[vertex2].append(vertex1)
            return True
        return False
        
    def Remove_Edge(self,vertex1,vertex2):
        if vertex1 in self.adjacent_list.keys() and vertex2 in self.adjacent_list.keys():
            try:  # in case there is no vertices connected  
                self.adjacent_list[vertex1].remove(vertex2)
                self.adjacent_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def Remove_Vertex(self,vertex):
        if vertex in self.adjacent_list.keys():
            for other_vertex in self.adjacent_list[vertex]:
                self.adjacent_list[other_vertex].remove(vertex)
            del self.adjacent_list[vertex]
            return True
        return False    


myG=Graph()
myG.AddVertex('A')
myG.AddVertex('B')
myG.AddVertex('C')
myG.AddVertex('D')

myG.Add_Edge('A','B')
myG.Add_Edge('A','C')
myG.Add_Edge('A','D')
myG.Add_Edge('B','D')
myG.Add_Edge('C','D')
# myG.Remove_Edge()
# myG.Remove_Vertex('D')
myG.printGraph()