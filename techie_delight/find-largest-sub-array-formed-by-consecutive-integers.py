#!/usr/bin/python

import sys

def main():
    arr = [2,0,2,1,4,3,1,0]
    print arr
    dict ={}
    max_sequence = []
    for i in range(len(arr)):
        for j in range(0, i+1):
            slice = arr[j:i+1]
            if is_consecutive(slice):
                if len(slice) > len(max_sequence):
                    max_sequence = slice
    print max_sequence
                
    
def is_consecutive(sub_arr):
    sub_set = set(sub_arr)
    if len(sub_set) != len(sub_arr):
        return False
    
    min = sub_arr[0]
    max = sub_arr[0]
    for num in sub_arr:
        if num < min:
            min = num
        if num > max:
            max = num
    for i in range(min, max+1):
        if i not in sub_set:
            return False
    return True
    
if __name__ == "__main__":
    main()
    
    