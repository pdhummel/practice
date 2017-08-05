#!/usr/bin/python


def main():
    arr = [8,7,2,5,3,1]
    sum = 10
    print arr
    
    dict = {}
    index = 0
    for i in arr:
        j = sum - i
        dict[i] = index
        if j in dict and dict[i] != dict[j]:
            print str(i) + " + " + str(j) + " found at " + str(dict[i]) + " and " + str(dict[j])
        index = index + 1

if __name__ == "__main__":
    main()
    
    