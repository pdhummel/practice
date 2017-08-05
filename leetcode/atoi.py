#!/usr/bin/python

import sys
import time


class Solution(object):
    def myAtoi(self, stri):
        """
        :type str: str
        :rtype: int
        """
        integer = 0
        if stri is None or len(stri) < 1:
            return integer
        
        stri = stri.strip()
        start = 0
        negative = False
        if stri[0] == "+":
            start = 1        
        if stri[0] == "-":
            negative = True
            start = 1
        for i in range(start, len(stri)):
            ascii_value = ord(stri[i])
            if ascii_value >= 48 and ascii_value <= 57:
                integer = integer * 10
                integer = integer + ord(stri[i]) - 48
            else:
                break
                
        if negative:
            integer = integer * -1

        # Limit to the size of a 32 bit signed number.
        if integer > 2147483647:
            integer = 2147483647
        if integer < -2147483648:
            integer = -2147483648
            
        return integer


def main(args):
    if len(args) > 1:
        s = args[1]
    else:
        s = ""
    
    start = time.clock()
    solution = Solution()
    
    integer = solution.myAtoi(s)
    print integer

    
    end = time.clock()
    elapsed_time = end - start
    print "The program took " + str(elapsed_time) + " seconds to execute."
     

    
if __name__ == "__main__":
    main(sys.argv)
    
    