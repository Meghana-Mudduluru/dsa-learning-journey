'''
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

    0 <= i < j < k < arr.length
    |arr[i] - arr[j]| <= a
    |arr[j] - arr[k]| <= b
    |arr[i] - arr[k]| <= c

Where |x| denotes the absolute value of x.
Return the number of good triplets.

Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

Example 2:
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
'''

from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        total = [0] * 1001
        for j in range(n):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    lj, rj = arr[j] - a, arr[j] + a
                    lk, rk = arr[k] - c, arr[k] + c
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)
                    if l <= r:
                        ans += total[r] if l == 0 else total[r] - total[l - 1]
            for k in range(arr[j], 1001):
                total[k] += 1

        return ans

# Create an object of the class
sol = Solution()

# Example input
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3

# Call the method
result = sol.countGoodTriplets(arr, a, b, c)
print("Number of good triplets:", result)
