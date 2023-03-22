class Hashtable:
    def __init__(self,size=7):
        self.hashmap=[None]*size

    def hashMethod(self,key):
        myhash=0
        for letter in key:
            myhash=(myhash+ord(letter)*23) %len(self.hashmap)   
        return myhash
    
    def setitem(self,key,value):
        index=self.hashMethod(key)
        if self.hashmap[index]==None:
            self.hashmap[index]=[]
        self.hashmap[index].append([key,value])    

    def printmap(self):
        for i in range(len(self.hashmap)):
            print(i,":",self.hashmap[i])    
    
    def getItem(self,key):
        index=self.hashMethod(key)
        for i in range(len(self.hashmap[index])):
            if self.hashmap[index][i][0]==key:
                return self.hashmap[index][i][1]
            
        return None    

    def allkeys(self):
        ak=[]
        for i in range(len(self.hashmap)):
            if self.hashmap[i] is not None:
                for j in range(len(self.hashmap[i])):
                    ak.append(self.hashmap[i][j][0])
                
        return ak

mytable=Hashtable()
mytable.setitem('ket',10)
mytable.setitem('kitty',130)
mytable.setitem('seset',22)
mytable.setitem('beeset',232)
mytable.setitem('bett',1560)
f=mytable.getItem('seset')
print(f)
mytable.printmap()
x=mytable.allkeys()
print(x)