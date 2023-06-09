#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if not root1 and not root2:
                return None
            if not root1 and root2:
                return root2
            if root1 and not root2:
                return root1
            if root1 and root2:
                root1.left = dfs(root1.left, root2.left)
                root1.right = dfs(root1.right, root2.right)
                root1.val = root1.val + root2.val
                return root1
        
        return dfs(root1, root2)
# @lc code=end

