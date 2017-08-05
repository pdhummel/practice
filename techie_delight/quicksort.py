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
        pivot = arr[len(arr)-1]
        left = []
        right = []
        
        for i in range(0, len(arr)-1):
            n = arr[i]
            if n < pivot:
                left.append(n)
            else:
                right.append(n)
        sorted_left = split_and_sort(left)
        sorted_right = split_and_sort(right)
        sorted_arr.extend(sorted_left)
        sorted_arr.append(pivot)
        sorted_arr.extend(sorted_right)
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
    
if __name__ == "__main__":
    main()
    
    