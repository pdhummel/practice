#!/usr/bin/python

import sys
import time



class Solution(object):
    def intToRoman(self, integer):
        """
        :type integer: int
        :rtype: roman
        """

        roman = ""

        roman, integer = self.process_segment(integer, roman, "M", 1000)
        roman, integer = self.process_segment(integer, roman, "CM", 900)
        roman, integer = self.process_segment(integer, roman, "D", 500)
        roman, integer = self.process_segment(integer, roman, "CD", 400)
        roman, integer = self.process_segment(integer, roman, "C", 100)
        roman, integer = self.process_segment(integer, roman, "XC", 90)
        roman, integer = self.process_segment(integer, roman, "L", 50)
        roman, integer = self.process_segment(integer, roman, "XL", 40)
        roman, integer = self.process_segment(integer, roman, "X", 10)
        roman, integer = self.process_segment(integer, roman, "IX", 9)
        roman, integer = self.process_segment(integer, roman, "V", 5)
        roman, integer = self.process_segment(integer, roman, "IV", 4)
        roman, integer = self.process_segment(integer, roman, "I", 1)

        return roman


    def process_segment(self, integer, roman, roman_segment, value):    
        if str(value)[0] == "1":
            count = integer / value
            integer = integer - count*value
            if count > 3 and roman_segment == "M":
                roman = roman + "*MMM"
            else:
                roman = roman + roman_segment * count
        else:
            if integer >= value:
                roman = roman + roman_segment
                integer = integer - value
        return roman, integer




def main(args):
    integer = 0
    if len(args) > 1:
        integer = int(args[1])
    
    start = time.clock()
    solution = Solution()
    

    roman = solution.intToRoman(integer)
    print roman
    
    end = time.clock()
    elapsed_time = end - start
    print "The program took " + str(elapsed_time) + " seconds to execute."
    
if __name__ == "__main__":
    main(sys.argv)
    