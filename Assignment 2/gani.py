# # Python3 program for building Heap from Array
 
# # To heapify a subtree rooted with node i
# # which is an index in arr[]. N is size of heap
 
 
# def heapify(arr, n, i):
 
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1  # left = 2*i + 1
#     r = 2 * i + 2  # right = 2*i + 2
 
#     # If left child is larger than root
#     if l < n and arr[l] > arr[largest]:
#         largest = l
 
#     # If right child is larger than largest so far
#     if r < n and arr[r] > arr[largest]:
#         largest = r
 
#     # If largest is not root
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
 
#         # Recursively heapify the affected sub-tree
#         heapify(arr, n, largest)
 
# # Function to build a Max-Heap from the given array
 
 
# def buildHeap(arr, n):
 
#     # Index of last non-leaf node
#     startIdx = n // 2 - 1
 
#     # Perform reverse level order traversal
#     # from last non-leaf node and heapify
#     # each node
#     for i in range(startIdx, -1, -1):
#         heapify(arr, n, i)
 
# # A utility function to print the array
# # representation of Heap
 
 
# def printHeap(arr, n):
#     print("Array representation of Heap is:")
 
#     for i in range(n):
#         print(arr[i], end=" ")
#     print()
 
 
# # Driver Code
# if __name__ == '__main__':
 
#     # Binary Tree Representation
#     # of input array
#     #             1
#     #           /    \
#     #         3        5
#     #       /  \     /  \
#     #     4      6  13  10
#     #    / \    / \
#     #   9   8  15 17
#     arr = [1, 3, 5, 4, 6, 13,
#             10, 9, 8, 15, 17]
#     # arr = [9.4, 9.3, 9.2, 9.1, 9.0, 9.0, 8.8, 8.8, 8.8, 8.8, 8.7, 8.7,
#     #  8.6, 8.6, 8.5, 8.5, 8.4, 8.4, 8.4, 8.4, 8.4, 8.4, 8.3, 8.2, 8.1, 8.0, 7.8, 7.7, 7.7, 7.5, 7.5, 7.4, 7.4, 7.4, 7.4, 7.3, 7.3, 7.2, 7.2, 7.2, 7.1]

#     # arr = [10.0, 7.2, 8.7, 9.0, 7.2, 7.3, 7.8, 7.7, 8.1, 9.4, 8.6, 7.3, 8.4, 8.5, 7.5, 8.8, 8.7, 8.4, 8.8, 8.8, 8.5, 
#     #     8.3, 7.4, 8.4, 8.8, 8.2, 8.4, 8.4, 7.2, 7.4, 8.4, 8.6, 9.3, 7.7, 9.0, 9.2, 7.4, 8.0, 7.1, 7.4, 9.1, 7.5]
#     n = len(arr)
 
#     buildHeap(arr, n)
 
#     printHeap(arr, n)
 
#     # Final Heap:
#     #             17
#     #           /    \
#     #         15      13
#     #        /  \     / \
#     #       9     6  5   10
#     #      / \   / \
#     #     4   8 3   1
 
# # This code is contributed by Princi Singh

# Heap Sort in python


# def heapify(arr, n, i):
#       # Find largest among root and children
#       largest = i
#       l = 2 * i + 1
#       r = 2 * i + 2
  
#       if l < n and arr[i] < arr[l]:
#           largest = l
  
#       if r < n and arr[largest] < arr[r]:
#           largest = r
  
#       # If root is not largest, swap with largest and continue heapifying
#       if largest != i:
#           arr[i], arr[largest] = arr[largest], arr[i]
#           heapify(arr, n, largest)
  
  
# def heapSort(arr):
#       n = len(arr)
  
#       # Build max heap
#       for i in range(n//2, -1, -1):
#           heapify(arr, n, i)
  
#       for i in range(n-1, 0, -1):
#           # Swap
#           arr[i], arr[0] = arr[0], arr[i]
  
#           # Heapify root element
#           heapify(arr, i, 0)
  
  
# arr = [10.0, 7.2, 8.7, 9.0, 7.2, 7.3, 7.8, 7.7, 8.1, 9.4, 8.6, 7.3, 8.4, 8.5, 7.5, 8.8, 8.7, 8.4, 8.8, 8.8, 8.5, 
#             8.3, 7.4, 8.4, 8.8, 8.2, 8.4, 8.4, 7.2, 7.4, 8.4, 8.6, 9.3, 7.7, 9.0, 9.2, 7.4, 8.0, 7.1, 7.4, 9.1, 7.5]

# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print("%d " % arr[i], end='')

# def heapsort(A):
#    build_max_heap(A)
#    for i in range(len(A) - 1, 0, -1):
#        #A[0], A[i] = A[i], A[0]
#        A[i], A[0] = A[i], A[0]
#        max_heapify(A, index=0, size=i)
# def parent(i):
#    return (i - 1)//2
# def left(i):
#    return 2*i + 1
# def right(i):
#    return 2*i + 2
# def build_max_heap(A):
#     length = len(A)
#     n = int((len(A)//2)-1)
#     for k in range(n, -1, -1):
#         max_heapify(A,k, size = length)
#    length = len(A)
#    start = parent(length - 1)
#    while start >= 0:
#        max_heapify(A, index=start, size=length)
#        start = start - 1
# def max_heapify(A, index, size):
#    largest = index
#    left_child = left(index)
#    right_child = right(index)
#    if (left_child < size and A[left_child] > A[index]):
#        largest = left_child
#    else:
#        largest = index
#    if (right_child < size and A[right_child] > A[largest]):
#        largest = right_child
#    if (largest != index):
#         A[index], A[largest] = A[largest], A[index]
#         max_heapify(A, largest, size)
# #A = input('Enter the list of numbers: ').split()
# A = [10.0, 7.2, 8.7, 9.0, 7.2, 7.3, 7.8, 7.7, 8.1, 9.4, 8.6, 7.3, 8.4, 8.5, 7.5, 8.8, 8.7, 8.4, 8.8, 8.8, 8.5, 
#         8.3, 7.4, 8.4, 8.8, 8.2, 8.4, 8.4, 7.2, 7.4, 8.4, 8.6, 9.3, 7.7, 9.0, 9.2, 7.4, 8.0, 7.1, 7.4, 9.1, 7.5]
# heapsort(A)
# print('Sorted list: ', end='')
# print(A)

# def sort_dict_by_value(dictionary):
#     """
#     Sort a dictionary by value.
#     """
#     return dict(sorted(dictionary.items(), key=lambda x: x[1]))

# def sort_dict_by_value_and_key_and_reverse(dictionary):
#     """
#     Sort a dictionary by value and key and reverse.
#     """
#     return dict(sorted(dictionary.items(), key=lambda x: (x[1], x[0]), reverse=True))

# if __name__ == "__main__":
#     fruits = {"orange": 300, "olives": 400, "apple": 500, "banana": 200, "kiwi": 400}
#     print("Sort by value:")
#     print(sort_dict_by_value(fruits))

#     print("Sort by value and key and reverse:")
#     print(sort_dict_by_value_and_key_and_reverse(fruits))


## Correct output

# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
 
 
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] > arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] > arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
 
 
# Driver code
arr = [10.0, 7.2, 8.7, 9.0, 7.2, 7.3, 7.8, 7.7, 8.1, 9.4, 8.6, 7.3, 8.4, 8.5, 7.5, 8.8, 8.7, 8.4, 8.8, 8.8, 8.5, 
         8.3, 7.4, 8.4, 8.8, 8.2, 8.4, 8.4, 7.2, 7.4, 8.4, 8.6, 9.3, 7.7, 9.0, 9.2, 7.4, 8.0, 7.1, 7.4, 9.1, 7.5]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print(arr[i])
