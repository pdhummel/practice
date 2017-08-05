#!/usr/bin/python

import sys

def main():
    arr = [1,2,3,4,4]
    arr = [1,2,3,4,2]
    print arr
    
    dict = {}
    for i in arr:
        if i in dict:
            print "duplicate " + str(i)
        else:
            dict[i] = True
    
if __name__ == "__main__":
    main()
    
    