from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        tree = {}
        for u, v in edges:
            if u not in tree:
                tree[u] = []
            if v not in tree:
                tree[v] = []
            tree[u].append(v)
            tree[v].append(u)

        def find_bob_path(node, parent):
            if node == 0:
                return [0]
            for neighbor in tree[node]:
                if neighbor != parent:
                    path = find_bob_path(neighbor, node)
                    if path:
                        return [node] + path
            return []

        bob_path = find_bob_path(bob, -1)
        bob_time = {node: t for t, node in enumerate(bob_path)}

        def dfs_alice(node, parent, time, income):
            if node in bob_time:
                if bob_time[node] > time:
                    income += amount[node]
                elif bob_time[node] == time:
                    income += amount[node] // 2
            else:
                income += amount[node]

            if len(tree[node]) == 1 and node != 0:
                return income

            max_income = float('-inf')
            for neighbor in tree[node]:
                if neighbor != parent:
                    max_income = max(max_income, dfs_alice(neighbor, node, time + 1, income))

            return max_income

        return dfs_alice(0, -1, 0, 0)

# Create an object and call the function
solution = Solution()
edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]
print(solution.mostProfitablePath(edges, bob, amount))