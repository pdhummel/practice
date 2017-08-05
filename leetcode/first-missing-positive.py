#!/usr/bin/python

import sys
import time


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        found_num = set()
        missing_num_set = set()
        missing_num_set.add(1)
        missing_num = 1
        
        for num in nums:
            if num > 0:
                found_num.add(num)
                
                if num in missing_num_set:
                    missing_num_set.remove(num)
                    missing_num_list = list(missing_num_set)
                    missing_num_list.sort()
                    if len(missing_num_list) > 0:
                        missing_num = missing_num_list[0]
                    else:
                        missing_num = None    
                        
                if num+1 not in found_num:
                    missing_num_set.add(num+1)
                    if missing_num is None or num+1 < missing_num:
                        missing_num = num+1
    
        return missing_num

    
def main(args):
    if len(args) > 1:
        pass
    
    start = time.clock()
    solution = Solution()
    
    nums = [1,2,0]
    nums = [3,4,-1,1]
    nums = []
    nums = [1]
    nums = [-1,4,2,1,9,10]
    nums = [44,48,31,53,24,56,6,18,33,20,-5,-2,-2,-2,53,-9,11,13,35,34,22,-6,28,11,44,52,43,42,-9,4,14,45,12,56,41,-4,5,7,42,49,55,47,7,13,55,4,14,9,27,-8,54,-8,13,42,31,17,37]
    
    missing_num = solution.firstMissingPositive(nums)
    print missing_num

    
    end = time.clock()
    elapsed_time = end - start
    print "The program took " + str(elapsed_time) + " seconds to execute."
    
if __name__ == "__main__":
    main(sys.argv)
    
    