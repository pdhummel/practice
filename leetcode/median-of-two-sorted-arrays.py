#!/usr/bin/python

#from __future__ import division
import sys
import time


class Solution(object):
    def findMedianSortedArrays(self, list1, list2):
        """
        :type list1: List[int]
        :type list2: List[int]
        :rtype: float
        """
        
        merged_list = []
        l1i = 0
        l2i = 0
        
        while l1i < len(list1) and l2i < len(list2):
            if list1[l1i] < list2[l2i]:
                merged_list.append(list1[l1i])
                l1i += 1
            else:
                merged_list.append(list2[l2i])
                l2i += 1
        while l1i < len(list1):
            merged_list.append(list1[l1i])
            l1i += 1
        while l2i < len(list2):
            merged_list.append(list2[l2i])
            l2i += 1


        median_idx = len(merged_list) / 2
        print merged_list, median_idx
        if len(merged_list) % 2 == 0:
            median_idx += -1
            median = (float(merged_list[median_idx]) + float(merged_list[median_idx+1])) / float(2)
        else:
            median = merged_list[median_idx]
        
        return median

def main(args):
    if len(args) > 1:
        pass
    
    start = time.clock()
    solution = Solution()
    
    l1 = [1, 2, 5, 9, 11]
    l2 = [3, 4, 7]
    
    #l1= [ 1,2 ]
    #l2= [ 3,4 ]
    
    #l1 = [1,3]
    #l2 = [2]
    median = solution.findMedianSortedArrays(l1, l2)
    
    end = time.clock()
    elapsed_time = end - start
    print "The program took " + str(elapsed_time) + " seconds to execute."
    
if __name__ == "__main__":
    main(sys.argv)
    
    