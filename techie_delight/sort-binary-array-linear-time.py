#!/usr/bin/python

import sys

def main():
    arr = [1,0,1,0,1,0,0,1]
    print arr 
    
    count0 = 0
    for i in arr:
        if i == 0:
            count0 = count0 + 1
    for i in range(count0):
        sys.stdout.write("0 ")
    for i in range(len(arr) - count0):
        sys.stdout.write("1 ")
    print ""
        
if __name__ == "__main__":
    main()
    
    