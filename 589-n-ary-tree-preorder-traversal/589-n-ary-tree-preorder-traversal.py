"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
def dfs(root, return_list):
        if root is None:
            return
        return_list.append(root.val)
        for child in root.children:
            dfs(child, return_list)
            
class Solution(object):
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return_list = []
        dfs(root, return_list)
        return return_list 
        
        
        