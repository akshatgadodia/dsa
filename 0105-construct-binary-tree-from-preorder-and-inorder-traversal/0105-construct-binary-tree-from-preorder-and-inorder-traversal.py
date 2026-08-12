# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_value = preorder[0]
        root = TreeNode(val=root_value)

        root_index = inorder.index(root_value)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        left_preorder = preorder[1:root_index+1]
        right_preorder = preorder[root_index + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

        