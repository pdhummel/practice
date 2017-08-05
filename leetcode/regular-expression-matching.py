#!/usr/bin/python

import sys
import time


class Solution(object):
    def isMatch(self, stringex, regex):
        """
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).        
        
        :type stringex: str
        :type regex: str
        :rtype: bool
        """
        
        stringex = stringex.strip()
        regex = regex.strip()
        
        if regex == "" and len(stringex) == 0:
            return True        
        elif regex == ".*" and len(stringex) == 0:
            return True
        elif len(regex) > 1 and regex[1] == "*" and len(stringex) == 0:
            pass
        elif len(stringex) == 0:
            return False       
        
        
        match = self.match_sub(stringex, regex, True)
        return match
        
    
    def match_sub(self, stringex, regex, first=False):
        #print stringex, regex
        match = True
        rulestr = ""        
        r = 0
        
        if len(regex) > 0:
            rulestr += regex[0]
            r += 1
        
        any_size = False
        if len(regex) > 1:
            if regex[1] == "*":
                any_size = True
                rulestr += regex[1]
                r += 1
        
        did_match, advance = self.evaluate_rule(stringex, rulestr)
        if did_match == False:
            return False

        
        if first:
            rule_chars = set()
            prev_char = ""
            for i in range(len(regex)):
                if regex[i] != "*" and prev_char != "*" and len(prev_char) > 0:
                    rule_chars.add(prev_char)
                prev_char = regex[i]
            if prev_char != "*" and len(prev_char) > 0:
                rule_chars.add(prev_char)

            for char in rule_chars:
                if char == ".":
                    continue
                if stringex.find(char) < 0:
                    return False
        
        
        rng = range(1, advance+1)
        if any_size:
            rng = range(0, advance+1)
        if advance == 0:
            rng = range(0, 1)
                    
        match = False
        for i in rng:  
            if i < len(stringex) and r < len(regex):
                match = self.match_sub(stringex[i:], regex[r:])
                #print 1, match
            else:
                if i < len(stringex) and r >= len(regex):
                    pass
                    #print 2, match
                elif i >= len(stringex) and r < len(regex):
                    match = self.match_sub("", regex[r:])
                    #print 3, match, regex[r:]
                else:
                    match = True
                    #print 4, match
            if match == True:
                break
        
        return match

    
    def evaluate_rule(self, stringseg, rule):
        #print "eval", stringseg, rule
        match = False
        advance = 0
        if len(rule) == 0:
            return True, 0
        if len(rule) > 1 and rule[1] == "*" and len(stringseg) == 0:
            return True, 0
        elif len(stringseg) == 0:
            return False, 0
        
        if len(rule) == 1:
            if rule == "." or rule == stringseg[0]:
                return True, 1
            else:
                return False, 0
        if len(rule) > 1:
            match = True
            if rule == ".*": # and len(stringseg) == 0:
                return True, len(stringseg)
            
            if rule[0] == stringseg[0]:
                char = stringseg[0]
                advance = 1
                while advance < len(stringseg) and stringseg[advance] == char:
                    advance += 1
        
        return match, advance

        
def main(args):
    if len(args) > 1:
        s = args[1]
        regex = args[2]
    else:
        print args[0], "stringex regex"
        sys.exit(1)
    #print s, regex
    
    start = time.clock()
    solution = Solution()
    
    rv = solution.isMatch(s, regex)
    print rv

    
    end = time.clock()
    elapsed_time = end - start
    print "The program took " + str(elapsed_time) + " seconds to execute."
     

    
if __name__ == "__main__":
    main(sys.argv)
    
    