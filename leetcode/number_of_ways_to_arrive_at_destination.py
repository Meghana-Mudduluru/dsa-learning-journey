'''
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.



Example 1:

Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

'''


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:

        MOD = 10 ** 9 + 7
        graph = {i: [] for i in range(n)}

        # Build adjacency list
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Priority queue (implemented as a list of tuples)
        queue = [(0, 0)]  # (time, node)
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1  # One way to reach start node

        while queue:
            # Find the node with the smallest current time
            queue.sort()  # Sorting ensures we always pick the shortest time first
            curr_time, node = queue.pop(0)

            # If a shorter route to `node` was already found, ignore this one
            if curr_time > dist[node]:
                continue

            for neighbor, time in graph[node]:
                new_time = curr_time + time

                # Found a shorter path to `neighbor`
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    queue.append((new_time, neighbor))

                # Found another shortest path to `neighbor`
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]

# Create an instance of the Solution class
solution = Solution()

# Define input values
n = 7
roads = [
    [0,6,7], [0,1,2], [1,2,3], [1,3,3], [6,3,3],
    [3,5,1], [6,5,1], [2,5,1], [0,4,5], [4,6,2]
]

# Call the method and print the result
result = solution.countPaths(n, roads)
print(result)  # Expected Output: 4
