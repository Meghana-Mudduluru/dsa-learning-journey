'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation:
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7.
Another possible subsequence is [4, 3].

'''

from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]  # auxiliary array
        # sort by numerical value in descending order
        vals.sort(key=lambda x: -x[1])
        # select the first k elements and sort them in ascending order by index
        vals = sorted(vals[:k])
        res = [val for idx, val in vals]  # target subsequence
        return res

nums = [-1,-2,3,4]
k = 3

sol=Solution()
print(sol.maxSubsequence(nums,k))