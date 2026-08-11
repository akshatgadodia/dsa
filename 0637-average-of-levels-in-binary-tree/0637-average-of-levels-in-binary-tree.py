from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []

        if root is None:
            return result

        queue = deque()
        queue.append(root)
        
        while queue:
            queue_length = len(queue)
            result.append(sum([ele.val for ele in queue]) / queue_length)
            for _ in range(queue_length):
                element = queue.popleft()

                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
        
        return result
        