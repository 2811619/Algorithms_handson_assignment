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
            
            # Implementing linear probing
            while self.hashtable[index] != None :
                index = (index+1)%10

            return index
        
    def insert(self,key) :
        
        index = self.hash(key)
        self.hashtable[index] = key
        
    def search(self,key) :
        
        index = key%10
        
        if self.hashtable[index] != key :
            while self.hashtable[index] != key and self.hashtable[index] != None :
                index = (index+1)%10
                
        if self.hashtable[index] == key :
            return index
        else :
            return None

    def contains(self, key) :
        #if self.hashtable[index] == key :
        tab = self.hashtable
        if (tab.__contains__(key)):
        #if self.hashtable[key] == index:
            print (True)
        else:
            print (False)
    
    def print_hashtable(self) :
        
        print("Hash table is:\n\nindex \t value")
        for x in range(len(self.hashtable)) :
            print(x,"\t\t\t",self.hashtable[x])

if __name__ == '__main__':
    # Initializing hash table of size 10
    HT = Hash_table(20)
    x = []
    with open('file1.txt', 'r') as f:
        x = [line.strip() for line in f]
    #print (x)
    for x in range(len(x)):
        HT.insert(x)
    # Inserting only 5 values to make λ <= 0.5
    # HT.insert(10)
    # HT.insert(90)
    # HT.insert(80)
    # HT.insert(44)
    # HT.insert(55)
    # HT.insert(57)
    # HT.insert(59)
    # HT.insert(61)
    # HT.insert(62)
    # HT.insert(64)

    HT.print_hashtable()

    HT.contains(10)
    index = HT.search(10)

    if index!= None :
        print("\nGiven key is present at index",index)
    else :
        print("\nGiven key is not present in the hash table")
