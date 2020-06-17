# https://leetcode.com/problems/split-a-string-in-balanced-strings/
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        L_count = 0
        R_count = 0
        
        max_balanced = 0
        
        for letter in s:
            
            if letter == 'R': R_count += 1
            else: L_count += 1
            
            # String is balanced and non-empty
            if L_count == R_count != 0:
                max_balanced += 1
                L_count = R_count = 0
                
        return max_balanced
