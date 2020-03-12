# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    @staticmethod
    def maxDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        max_depth = 0
        
        # Compute depth of each subtree
        l_depth = Solution.maxDepth(root.left)
        r_depth = Solution.maxDepth(root.right)
        
        if l_depth > r_depth:  # Left subtree is larger
            return l_depth+1
        else:                  # Right subtree is larger
            return r_depth+1
