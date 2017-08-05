#!/usr/bin/python

import sys



def main():
    arr = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    print arr
    sorted_arr = split_and_sort(arr)
    print sorted_arr

    
def split_and_sort(arr):
    sorted_arr = []
    if len(arr) > 2:
        midpoint = len(arr)/2
        left = arr[0:midpoint]
        right = arr[midpoint:]
        sorted_left = split_and_sort(left)
        sorted_right = split_and_sort(right)
        sorted_arr = merge(sorted_left, sorted_right)
    elif len(arr) == 2:
        if arr[0] < arr[1]:
            sorted_arr.append(arr[0]) 
            sorted_arr.append(arr[1]) 
        else:
            sorted_arr.append(arr[1]) 
            sorted_arr.append(arr[0]) 
    elif len(arr) == 1:
        sorted_arr.append(arr[0])
    return sorted_arr

def merge(left, right):
    sorted_arr = []
    li = 0
    ri = 0
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            sorted_arr.append(left[li])
            li = li + 1
        else:
            sorted_arr.append(right[ri])
            ri = ri + 1
    if li >= len(left):
        sorted_arr.extend(right[ri:])
    else:
        sorted_arr.extend(left[li:])
    return sorted_arr
        
if __name__ == "__main__":
    main()
    
    