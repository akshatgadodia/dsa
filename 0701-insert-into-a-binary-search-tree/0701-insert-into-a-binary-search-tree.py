# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return TreeNode(val=val)

        def traverse(node):
            if node is None:
                return
            
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val=val)
                else:
                    traverse(node.right)
            else:
                if node.left is None:
                    node.left = TreeNode(val=val)
                else:
                    traverse(node.left)

        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val=val)
                return root
            traverse(root.left)
        else:
            if root.right is None:
                root.right = TreeNode(val=val)
                return root
            traverse(root.right) 

        return root 