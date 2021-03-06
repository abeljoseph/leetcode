# https://leetcode.com/problems/sort-array-by-parity/
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        array = []
        for num in A:
            # Odd
            if num % 2: array.append(num)
            # Even
            else: array.insert(0, num)
                
        return array
