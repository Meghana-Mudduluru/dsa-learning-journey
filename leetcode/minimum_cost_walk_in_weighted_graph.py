'''
There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.



Example 1:

Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

Output: [1,-1]

Explanation:

To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).

In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

Example 2:

Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]

Output: [0]

Explanation:

To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).

'''


class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Step 1: Find connected components and store min AND-value for each component
        visited = [-1] * n  # Stores component ID
        component_and_value = {}  # Stores min AND-value for each component
        component_id = 0

        def bfs(start):
            queue = [start]
            visited[start] = component_id
            min_and = (1 << 31) - 1  # Max 32-bit integer

            nodes_in_component = []

            while queue:
                node = queue.pop(0)
                nodes_in_component.append(node)

                for neighbor, weight in graph[node]:
                    min_and &= weight  # Compute AND value

                    if visited[neighbor] == -1:
                        visited[neighbor] = component_id
                        queue.append(neighbor)

            # Assign the min AND value to this component
            for node in nodes_in_component:
                component_and_value[node] = min_and

        # Identify connected components
        for i in range(n):
            if visited[i] == -1:  # Unvisited node, start BFS
                bfs(i)
                component_id += 1  # Move to next component

        # Step 2: Answer the queries
        result = []
        for s, t in query:
            if visited[s] == visited[t]:  # Same connected component
                result.append(component_and_value[s])
            else:
                result.append(-1)  # No path

        return result

# Sample input
n = 5
edges = [[0,1,7],[1,3,7],[1,2,1]]
query = [[0,3],[3,4]]

# Create an object of Solution class
sol = Solution()

# Call the function and print the result
output = sol.minimumCost(n, edges, query)
print(output)  # Expected Output: [1, -1]
