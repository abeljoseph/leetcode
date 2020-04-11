# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        
        subtraction_cases = {
            'IV':4, 
            'IX':9, 
            'XL':40, 
            'XC':90, 
            'CD':400, 
            'CM':900
        }
        
        num = 0
        
        for case in subtraction_cases:
            if case in s:
                num += subtraction_cases[case]
                s = s.replace(case, "")
            
        for numeral in s:
            num += roman_to_int[numeral]
            
        return num
