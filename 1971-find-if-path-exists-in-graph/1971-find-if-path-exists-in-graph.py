from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        visited = [False] * n

        for [e1, e2] in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        def dfs(node):
            if node == destination:
                return True
            
            if visited[node]:
                return False
            
            visited[node] = True
            
            for neighbour in adj[node]:
                if dfs(neighbour):
                    return True
            
            return False
        
        return dfs(source)
        