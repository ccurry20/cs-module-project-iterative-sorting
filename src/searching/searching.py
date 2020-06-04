def linear_search(arr, target):
    # Your code here
    #Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    #If x matches with an element, return the index.
    #If x doesn’t match with any of elements, return -1.
    for i in range(len(arr)): 
        if arr[i] == target: 
            return i 
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    #first item in arr
    low = 0
    #last item in list
    high = len(arr) - 1
    #while the low pointer is less than or equal to the high pointer
    while low <= high:
        #get middle index
        middle = (low + high) // 2
        #get item with the middle index
        guess = arr[middle]
        #if equals target, it is correct, return
        if guess == target:
            return middle
        #if too large, return high as index below middle
        if guess > target:
            high = middle - 1
        else:
        #else too low, change to index above middle
            low = middle + 1
    return -1  # not found
