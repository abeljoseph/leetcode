# https://leetcode.com/problems/flood-fill/
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        old = image[sr][sc]
            
        def dfs(image,i,j,newColor):
            
            if i<0 or i>= len(image) or j<0 or j>=len(image[0]):
                return
            if image[i][j] == newColor:
                return
            if image[i][j] == old:
                image[i][j] = newColor
                dfs(image,i+1,j,newColor)
                dfs(image,i-1,j,newColor)
                dfs(image,i,j+1,newColor)
                dfs(image,i,j-1,newColor)
    
        dfs(image,sr,sc,newColor)
        return image
        
