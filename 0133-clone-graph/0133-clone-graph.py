"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        nodes = {}

        def dfs(graph_node):
            if graph_node is None:
                return None

            value = graph_node.val
            if value in nodes:
                return nodes[value]
            
            current_node = Node(val=value)
            nodes[value] = current_node

            neighbours = []
            for neighbour in graph_node.neighbors:
                neighbour_copy = dfs(neighbour)
                if neighbour_copy:
                    neighbours.append(neighbour_copy)
            
            current_node.neighbors = neighbours
            return current_node
        
        return dfs(node)
        