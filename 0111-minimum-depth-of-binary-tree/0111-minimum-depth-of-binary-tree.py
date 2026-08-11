from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        result = 0

        queue = deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):
                element = queue.popleft()

                if not(element.left or element.right):
                    return result + 1

                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            
            result += 1
        
        return result

        