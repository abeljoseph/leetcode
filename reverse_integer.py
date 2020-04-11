# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x < -(2**31)) or (x > 2**31 -1): return 0
        
        negative = False
        
        # Deal with negative case
        if x < 0: 
            negative = True
            x = -x
            
        reversed_num = 0
        
        while (x > 0):
            num = x % 10  # get the last digit
            x = int(x/10)
            
            reversed_num = reversed_num*10 + num
            
        if (reversed_num < -(2**31)) or (reversed_num > 2**31 -1): return 0
        
        if negative: return reversed_num*-1
        return reversed_num
        
