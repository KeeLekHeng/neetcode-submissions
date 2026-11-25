# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return 0
            
            if node.left:
                left = dfs(node.left)
            arr.append(node.val)

            if node.right:
                right = dfs(node.right)
        dfs(root)
        return arr[k-1]
            

