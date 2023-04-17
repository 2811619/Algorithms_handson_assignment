from doctest import Example
import math

def max_heapify(A,n,k):
    largest =k
    l = left(k)
    r = right(k)
    if l < n and A[largest] > A[l]:
        largest = l

    if r < n and A[largest] > A[r]:
        largest = r

    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, n, largest)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_max_heap(A):
    n = len(A)
    # Build a maxheap.
    for k in range(n//2 - 1, -1, -1):
        max_heapify(A, n, k)
 
    # One by one extract elements
    for k in range(n-1, 0, -1):
        A[k], A[0] = A[0], A[k]  # swap
        max_heapify(A, k, 0)


def sortNamesAndRatings(name_dict):
    #sorted_example = sorted(name_dict.items(), key=lambda x: x[1],reverse=True)
    sorted_example = sorted(name_dict.keys(),key=lambda x: -name_dict[x])
    return sorted_example
# def sortNamesAndRatings(sorted_ratings, names):
# #sorted_example = sorted(name_dict.items(), key=lambda x: x[1],reverse=True)
#     sorted_example = sorted(name_dict.keys(),key=lambda x: -name_dict[x])
#     return sorted_example

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
    #print (name_dict_sort)
    build_max_heap(ratings)
    sorted_ratings = ratings
    sorted_names = []
    sorted_names = sortNames(name_dict_sort,sorted_ratings)
    return sorted_names
    