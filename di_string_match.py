# https://leetcode.com/problems/di-string-match/

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        a, b = 0, len(S) # creates pointers
        result = []
        for i in S:  # looking at each char, either append the the low or high pointer value, then increment or decrement
            if i=="I":
                result.append(a) 
                a+=1
            if i =="D":
                result.append(b)
                b-=1
        result.append(a)  # append the last digit that's left over (can be either a or b)
        return result
            
