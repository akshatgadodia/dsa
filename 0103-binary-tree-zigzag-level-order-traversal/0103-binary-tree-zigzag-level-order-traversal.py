from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        counter = 1

        queue = deque()
        queue.append(root)

        while queue:
            current = []
            for _ in range(len(queue)):
                element = queue.popleft()
                current.append(element.val)

                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            if counter % 2 == 0:
                result.append(current[::-1])
            else:
                result.append(current)
            counter += 1
        
        return result
