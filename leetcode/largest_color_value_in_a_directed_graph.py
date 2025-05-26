'''
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.



Example 1:

Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:

Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.

'''

from collections import deque, defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        # Build graph and indegree
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # DP table: dp[i][c] = max count of color c (0-25) ending at node i
        dp = [[0] * 26 for _ in range(n)]
        queue = deque()

        # Initialize queue with nodes having zero indegree
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for nei in graph[node]:
                for c in range(26):
                    dp[nei][c] = max(dp[nei][c], dp[node][c] + (1 if c == ord(colors[nei]) - ord('a') else 0))
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
            max_color_value = max(max_color_value, max(dp[node]))

        return max_color_value if visited == n else -1

colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]
sol=Solution()
print(sol.largestPathValue(colors,edges))