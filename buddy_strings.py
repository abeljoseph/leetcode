# https://leetcode.com/problems/buddy-strings/
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        if A == B: return len(set(A)) < len(A)
        
        count = 0
        arr = []
        
        for i, letter in enumerate(A):
            if B[i] != letter:
                count += 1
                arr.extend([letter, B[i]])
        
        if count > 2: return False
        
        return arr[0] == arr[3] and arr[1] == arr[2]                 
        
