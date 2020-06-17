# https://leetcode.com/problems/jewels-and-stones/
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """        
        jewel_count = 0
        
        for jewel in J:
            matching = [x for x in S if x==jewel]
            jewel_count += len(matching)
            
        return jewel_count
        
