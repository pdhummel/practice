#!/usr/bin/python

import sys

def main():
    arr = [4,2,-3,-1,0,4]
    dict = {}
    sequences = []
    
    for i in range(len(arr)):
        for j in range(0,i+1):
            if j in dict:
                dict[j] = dict[j] + arr[i]
            else:
                dict[j] = arr[i]
            if dict[j] == 0:
                sequences.append([j,i])
                
    for seq in sequences:
        j = seq[0]
        i = seq[1]
        for i in range(j,i+1):
            sys.stdout.write(str(arr[i]) + ' ')
        print ""
if __name__ == "__main__":
    main()
    
    