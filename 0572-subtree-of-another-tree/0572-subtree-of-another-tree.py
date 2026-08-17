# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(root_node, subRoot_node):
            if root_node is None and subRoot_node is None:
                return True

            if root_node is None or subRoot_node is None:
                return False
            
            if root_node.val != subRoot_node.val:
                return False
            
            return same_tree(
                root_node.left, subRoot_node.left
            ) and same_tree(
                root_node.right, subRoot_node.right
            )

        def dfs(node):
            if node is None:
                return False
            
            result = False
            if node.val == subRoot.val:
                result = same_tree(node, subRoot)

            left_tree = dfs(node.left)
            right_tree = dfs(node.right)

            return result or left_tree or right_tree
        
        return dfs(root)