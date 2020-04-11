# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = f"{x:031b}"
        bin_y = f"{y:031b}"
        
        h_dist = 0
        for i, letter in enumerate(bin_x):
            if not letter == bin_y[i]:
                h_dist += 1
                
        return h_dist
