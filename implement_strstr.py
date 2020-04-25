# https://leetcode.com/problems/implement-strstr/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "": return 0
        if needle not in haystack: return -1
        
        for i, letter in enumerate(haystack):
            if needle == haystack[i:len(needle)+i]: return i