# https://leetcode.com/problems/to-lower-case/

class Solution(object):
    def toLowerCase(self, str_):
        """
        :type str_: str
        :rtype: str
        """
        lower = list('abcdefghijklmnopqrstuvwxyz')
        upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
        string = ""
        
        for char in str_:
            if char in upper:
                index = upper.index(char)
                string += lower[index]
            else: string += char
                
        return string
            
