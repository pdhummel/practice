#!/usr/bin/python

import sys
import ctypes



def main(args):
    if len(args) > 1:
        reverse_string(args[1])
    
def reverse_string(str2rev):    
    mutable = ctypes.create_string_buffer(str2rev)
    
    for i in range(len(str2rev)):
        j = len(str2rev) - i - 1
        if i >= j:
            break
        left = mutable[i]
        right = mutable[j]
        mutable[i] = right
        mutable[j] = left
    
    print mutable.value
    
if __name__ == "__main__":
    main(sys.argv)
    
    