import math
from collections import defaultdict

class MaxHeap:
 
    def __init__(self, names, ratings):
        self.names = names
        self.ratings = ratings
 
    def parent(k):
        return (k-1)/2

    def leftChild(k):
        return 2 * k + 1

    def rightChild(k):
        return 2 * k + 2

    def maxHeapify(A, n, k):
        #Assigning left right and largest as k from buildMaxHeap
        largest = k
        left = MaxHeap.leftChild(k)
        right = MaxHeap.rightChild(k)
        if left < n and A[largest] > A[left]:
            largest = left
        
        if right < n and A[largest] > A[right]:
            largest = right

        if largest != k:
            A[k], A[largest] = A[largest], A[k]
            MaxHeap.maxHeapify(A, n, largest)
 
    def insert(A, n, k):
        n = n + 1
 
        #Insert the element at end of Heap
        A[n - 1] = k
 
        #Heapify the new node following a
        MaxHeap.maxHeapify(A, n, n - 1)
 
    #print nodes from top to down, left to right
    def Print(names, ratings):
        name_dict_sort ={}   
        for i in range(len(names)):
            name_dict_sort[names[i]] = ratings[i]
        MaxHeap.maxHeap(ratings)
        #MaxHeap.Print(ratings, names)
        sorted_ratings = ratings
        sorted_names = sortNames(name_dict_sort,sorted_ratings)
        names = sorted_names
        return names
    
    #constructe a max heap from array
    def maxHeap(A):
        n = len(A)
        for k in range(n//2 - 1, -1, -1):
            MaxHeap.maxHeapify(A, n, k)
 
        for k in range(n-1, 0, -1):
            A[k], A[0] = A[0], A[k]
            MaxHeap.maxHeapify(A, k, 0)

    def remove(A):
        global n
        # Get the last element
        lastElement = A[n - 1]
        # Replace root with last element
        A[0] = lastElement
        # Decrease size of heap by 1
        n = n - 1
        # heapify the root node
        MaxHeap.maxHeapify(A, n, 0)

# This method is used to assign the ratings to the movies and print the movie names
def sortNames(name_dict_sort, sorted_ratings):
    #print (name_dict_sort)
    #print (sorted_ratings)
    key_list = list(name_dict_sort.keys())
    val_list = list(name_dict_sort.values())
    names=[]
    for i in sorted_ratings:
        position= val_list.index(i)
        names.append(key_list[position])
    return names
 
def sort_movies_batch(names, ratings):
    name_dict_sort ={}   
    for i in range(len(names)):
        name_dict_sort[names[i]] = ratings[i]
    MaxHeap.maxHeap(ratings)
    #MaxHeap.Print(ratings, names)
    sorted_ratings = ratings
    sorted_names = sortNames(name_dict_sort,sorted_ratings)
    names = sorted_names
    return names

def sort_movies_incre(names, ratings):
    #To add movies directly, I took an iput from here which will 
    # name = input("Enter the movie name:")
    # rating = input("Enter the rating of the movie:")
    # names.append(name)
    # ratings.append(float(rating))
    # print (names)
    #print (ratings)
    #In the increment function, I added one rating and checked the output. It's sorted again.
    for i in ratings:
        MaxHeap.maxHeap(ratings)
    #print (ratings)
    #MaxHeap.Print(ratings, names)
    name_dict_sort ={}   
    for i in range(len(names)):
        name_dict_sort[names[i]] = ratings[i]
    MaxHeap.maxHeap(ratings)
    sorted_ratings = ratings
    sorted_names = sortNames(name_dict_sort,sorted_ratings)
    return sorted_names
