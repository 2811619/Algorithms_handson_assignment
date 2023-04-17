import numpy as np

class Hash_table() :
    
    def __init__(self,size) :
        self.size = size
        self.hashtable = np.array([None]*self.size)
        
    def hash(self,key) :
        
        # Hash function h(x) = x%10
        index = key%10 
        
        if self.hashtable[index] == None :
            return index
        else :
            i = 1
            # Implementing Double probing
            while self.hashtable[(index+(i*index))%10] != None :
                i += 1
                return (index+(i*index))%10
        
    def insert(self,key) :
        
        index = self.hash(key)
        self.hashtable[index] = key
        
    def search(self,key) :
        
        index = key%10
        
        i = 0
        if self.hashtable[index] != key :
            while self.hashtable[(index+(i*index))%10] != key and self.hashtable[(index+(i*index))%10] != None :
                i += 1
                
        if self.hashtable[(index+(i*index))%10] == key :
            return (index+(i*index))%10
        else :
            return None
    
    def print_hashtable(self) :
        
        print("Hash table:\n\nindex \t value")
        for x in range(len(self.hashtable)) :
            print(x,"\t\t",self.hashtable[x])

# Initializing hash table of size 10
HT = Hash_table(10)

# Inserting only 4 values to make λ <= 0.5
HT.insert(1)
HT.insert(2)
HT.insert(3)
HT.insert(4)
HT.insert(10)
HT.insert(20)


HT.print_hashtable()

index = HT.search(10)

if index!= None :
    print("\nGiven key is present at index",index)
else :
    print("\nGiven key is not present in the hash table")