# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Get the shortest string and save it in a variable
        shortest = ""
        
        for string in strs:
            if len(shortest) == 0:
                shortest = string
            elif len(shortest) > len(string):
                shortest = string
                
        # Create an interable which includes the whole string, all but the last letter, etc. and check whether the substring is in all the strings
        
        for i in reversed(range(len(shortest))):
            substring = shortest[:i+1]
            contains_substring = False
            for string in strs:
                if string.startswith(substring):
                    contains_substring = True
                else:
                    contains_substring = False
                    break
            if(contains_substring): return substring  
            
        return ""
        
