import time
import matplotlib.pyplot as plt
from numpy.random import randint
from heap import * 
if __name__ == "__main__":


    a_file = open("title.ratings.txt")
    names, ratings = [], []
    next(a_file)
    name_score_dict ={}
    for line in a_file:
        temp = line.rstrip().split('; ')
        names.append(temp[0]) #key: name
        ratings.append(float(temp[1])) #name: rating
        name_score_dict[temp[0]] = float(temp[1])
        #print (name_score_dict["Don't Look Up"])

    ########you need to design sort_movies() function    
    #sorted_names = sort_movies_batch(names, ratings)
    elements = list()
    times = list()
    start = time.perf_counter()
    sorted_names = sort_movies_batch(names, ratings)
    end = time.perf_counter()
    print(len(ratings), "Elements Sorted by HeapSort in ", end-start)
    sorted_names1 = sort_movies_incre(names, ratings)
    #print (sorted_names1)
    ################################################
    
    sorted, sorted1 = [], []
    for item in sorted_names:
        sorted.append(name_score_dict[item])
    print ("Sorted for sort_movie_batch(by using heap sort):", sorted)
    for item in sorted_names1:
        sorted1.append(name_score_dict[item])
    # print (sorted1)
    sorted_true = [9.4, 9.3, 9.2, 9.1, 9.0, 9.0, 8.8, 8.8, 8.8, 8.8, 8.7, 8.7,
     8.6, 8.6, 8.5, 8.5, 8.4, 8.4, 8.4, 8.4, 8.4, 8.4, 8.3, 8.2, 8.1, 8.0, 7.8, 7.7, 7.7, 7.5, 7.5, 7.4, 7.4, 7.4, 7.4, 7.3, 7.3, 7.2, 7.2, 7.2, 7.1]
    if sorted == sorted_true and sorted1 == sorted_true:
        print("pass")
    else:
        print("Not pass")

    # To plot the time complexity
    elements = list()
    times = list()
    for i in range(1, 10):
        a = randint(0, 100 * i, 100 * i)
        start =  time.perf_counter()
        MaxHeap.maxHeap(a)
        end =  time.perf_counter()
        elements.append(len(a))
        times.append(end-start)
    plt.xlabel('List Length')
    plt.ylabel('Time Complexity')
    plt.plot(elements, times, label ='Heap Sort')
    plt.grid()
    plt.legend()
    plt.show()
    plt.xlabel('List Length')
    plt.ylabel('Time Complexity')
    plt.plot(elements, times, label ='Heap Sort')
    plt.grid()
    plt.legend()
    plt.show()
    
