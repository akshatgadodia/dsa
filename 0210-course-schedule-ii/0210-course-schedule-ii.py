from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
            indegree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbour in adj[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(result) != numCourses:
            return []

        return result