'''
There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

    Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
        nums[u] = nums[u] XOR k
        nums[v] = nums[v] XOR k

Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.



Example 1:

Input: nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]
Output: 6
Explanation: Alice can achieve the maximum sum of 6 using a single operation:
- Choose the edge [0,2]. nums[0] and nums[2] become: 1 XOR 3 = 2, and the array nums becomes: [1,2,1] -> [2,2,2].
The total sum of values is 2 + 2 + 2 = 6.
It can be shown that 6 is the maximum achievable sum of values.

Example 2:

Input: nums = [2,3], k = 7, edges = [[0,1]]
Output: 9
Explanation: Alice can achieve the maximum sum of 9 using a single operation:
- Choose the edge [0,1]. nums[0] becomes: 2 XOR 7 = 5 and nums[1] become: 3 XOR 7 = 4, and the array nums becomes: [2,3] -> [5,4].
The total sum of values is 5 + 4 = 9.
It can be shown that 9 is the maximum achievable sum of values.

Example 3:

Input: nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
Output: 42
Explanation: The maximum achievable sum is 42 which can be achieved by Alice performing no operations.

'''

from typing import List
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sumVal = 0
        count = 0
        positiveMinimum = 1 << 30
        negativeMaximum = -1 * (1 << 30)

        for nodeValue in nums:
            operatedNodeValue = nodeValue ^ k
            sumVal += nodeValue
            netChange = operatedNodeValue - nodeValue
            if netChange > 0:
                positiveMinimum = min(positiveMinimum, netChange)
                sumVal += netChange
                count += 1
            else:
                negativeMaximum = max(negativeMaximum, netChange)

        # If the number of positive netChange values is even, return the sum.
        if count % 2 == 0:
            return sumVal

        # Otherwise return the maximum of both discussed cases.
        return max(sumVal - positiveMinimum, sumVal + negativeMaximum)

nums = [1,2,1]
k = 3
edges = [[0,1],[0,2]]
sol=Solution()
print(sol.maximumValueSum(nums,k,edges))