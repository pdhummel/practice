#!/usr/bin/python

import sys



def main():
    input = [ "CATGC", "CTAAGT", "GCTA", "TTCA", "ATGCATC" ] 
    # Answer: GCTAAGTTCATGCATC

    # (2^N N=len(list)), factorial time
    
    # Go through each permutation of the input list
    #    n!
    # -------- = 5! = 5*4*3*2 = 120 permutations
    # (n - r)!
    
    
    shortest = None
    
    # For each permutation
    for a in perm2(range(len(input)), 5):
        
        # Concatenate entries 2 at a time
        word = ""
        first = 0
        second = 1
        while second < len(input):
            # TODO: Remove repeating patterns found at end of first string and beginning of second string
            
            
            word = word + input[first] + input[second]
            first = second
            second = second + 1
            
        # Validate that each substring can still be found in the concatenated string
        ok = True
        for sub in input:
            if not sub in word:
                ok = False
        if ok:
            if shortest == None or len(word) < len(shortest):
                shortest = word
    print shortest

    
def perm2(A, k):
    r = [[]]
    for i in range(k):
        r = [[a] + b for a in A for b in r if a not in b]
    return r


    
# https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
def permute_in_place(a):
    a.sort()
    yield list(a)

    if len(a) <= 1:
        return

    first = 0
    last = len(a)
    while 1:
        i = last - 1

        while 1:
            i = i - 1
            if a[i] < a[i+1]:
                j = last - 1
                while not (a[i] < a[j]):
                    j = j - 1
                a[i], a[j] = a[j], a[i] # swap the values
                r = a[i+1:last]
                r.reverse()
                a[i+1:last] = r
                yield list(a)
                break
            if i == first:
                a.reverse()
                return
            
if __name__ == "__main__":
    main()
    
    