from collections import defaultdict

def number_of_connected_components_in_an_undirected_graph(n: int, edges: list[list[int]]) -> int:
    adj = defaultdict(list)
    result = 0

    for edge in edges:
        adj[edge[0]].append(edge[1]) 
        adj[edge[1]].append(edge[0]) 

    visited = [False] * n

    def dfs(node):
        if visited[node]:
            return

        visited[node] = True

        for neighbour in adj[node]:
            dfs(neighbour)
    
    for node in range(n):
        if not visited[node]:
            dfs(node)
            result += 1 
    
    return result

if __name__ == "__main__":
    n = int(input())
    edges = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = number_of_connected_components_in_an_undirected_graph(n, edges)
    print(res)
