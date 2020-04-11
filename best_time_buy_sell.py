# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        mn = 2**31
        
        for i, num in enumerate(prices):
            if num < mn: mn = num
            
            # get difference btw num and min
            diff = num - mn 
            
            # check whether num - min is greater than max_profit
            if diff > max_profit:
                max_profit = diff
            
        
        return max_profit
            
