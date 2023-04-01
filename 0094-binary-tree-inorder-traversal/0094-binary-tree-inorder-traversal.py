# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, return_list):
        if root:
            self.helper(root.left, return_list)
            return_list.append(root.val)
            self.helper(root.right, return_list)
            
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_list = []
        self.helper(root, return_list)
        return return_list
