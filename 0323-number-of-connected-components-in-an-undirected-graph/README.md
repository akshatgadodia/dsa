<h2><a href="https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph">323. Number of
Connected Components in an Undirected Graph</a></h2><h3>Med</h3><hr><p>You are given a graph with n nodes labeled from 0
to n-1. The graph is represented by an integer n (the number of nodes) and an array edges, where each element
edges[i] = [ai, bi] indicates that there is an undirected edge connecting nodes ai and bi.</p>

<p>Your task is to find and return the total number of connected components in the graph.</p>

<p>A connected component is a group of nodes where there is a path between any two nodes in the group, and these nodes are not connected to any other nodes outside the group. In other words, it's a maximal set of nodes that are all reachable from each other through the edges.</p>

<p>For example, if you have 5 nodes (0, 1, 2, 3, 4) and edges [[0,1], [2,3]], there would be 3 connected components:
<ul>
<li>Component 1: nodes {0, 1} (connected by an edge)</li>
<li>Component 2: nodes {2, 3} (connected by an edge)</li>
<li>Component 3: node {4} (isolated node with no edges)</li>
</ul>
</p>

<p>The solution uses Depth-First Search (DFS) to traverse the graph. It builds an adjacency list from the edges, then visits each node. When it encounters an unvisited node, it performs DFS to mark all nodes in that connected component as visited, counting this as one component. The process continues until all nodes have been visited, and the total count of components is returned.</p>
