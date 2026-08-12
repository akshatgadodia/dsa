class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return isConnected
        
        n = len(isConnected)

        visited = [False] * n
        result = 0

        def dfs(city):
            visited[city] = True

            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)

        for city in range(n):
            if not visited[city]:
                result += 1
                dfs(city)

        return result
        