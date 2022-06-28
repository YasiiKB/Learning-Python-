'''
Binary Search follows a "divide and conquer" logic.

The basic steps to perform Binary Search are:
1. Begin with an interval covering the whole array.
2. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
3. Otherwise, narrow it to the upper half.
4. Repeatedly check until the value is found or the interval is empty.

Binary Search vs. Naive Search:  Naive Search scans through all the array to find something, and is a lot slower than Binary search.
'''
import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    # We will leverage the fact that our list is SORTED
    if low is None:
        low = 0
    
    if high is None:
        high = len(l) - 1
    
    # Since we're adding 1 to midpoint and subtract 1 from it: 
    if high < low:
        return -1

    # eample l = [1, 3, 5, 10, 15] #looking for 5
    midpoint = (low + high) // 2 

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]: #look in the left hand half, from low upto (not including) the midpoint
        return binary_search(l, target, low, midpoint-1)
    else: #look in the right hand half, from (not including) the midpoint to high
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__': #is this file being run directry? if yes, then run this code.
    
    # build a sorted list of length 1000 for testing
    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # How long does it take to do the Naive search? 
    start = time.time() #gets the time right now.
    for target in sorted_list: # will run 1000 times (1000 iterations)!
        naive_search(sorted_list, target)
    end = time.time()
    print ('Naive search time:', (end - start)/length, 'seconds') #per iteration

    # How long does it take to do the Binary search? 
    start = time.time() #gets the time right now.
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print ('Binary search time:', (end - start)/length, 'seconds') #per iteration
