class Hashtable:
    def __init__(self,size=7):
        self.hash_map=[None]*size

    def hash_method(self,key) :
        myHash=0
        for letter in key:
            myHash=(myHash+ord(letter)*23)%(len(self.hash_map))

        return myHash

    def printmap(self):
        for i in range(len(self.hash_map)):
            print(i,":",self.hash_map[i]) 

    def set_items(self,key,value):
        index=self.hash_method(key)
        if self.hash_map[index]==None:
            self.hash_map[index]=[]
        self.hash_map[index].append([key,value])

    def gwt_items(self,key):
        index=self.hash_method(key)
        if self.hash_map[index] is not None:
            for i in range(len(self.hash_map)):    
                if self.hash_map[index][i][0]==key:
                    return self.hash_map[index][i][1]
        else:
            return None
        
    def allkeys(self):
        ak=[]
        for i in range(len(self.hash_map)):
            if self.hash_map[i]is not None:
                for j in range(len(self.hash_map[i])):
                    ak.append(self.hash_map[i][j][0]) 
        return ak               

hm=Hashtable()
hm.set_items('rock',10)
hm.set_items('paper',110)
hm.set_items('scissors',130)
hm.set_items('kick',140)
x=hm.gwt_items('paper')
hm.printmap()
print(x)
x2=hm.allkeys()
print(x2)