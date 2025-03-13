'''
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

    Decrement the value at each index in the range [li, ri] in nums by at most vali.
    The amount by which each value is decremented can be chosen independently for each index.

A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.



Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

    For i = 0 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
        The array will become [1, 0, 1].
    For i = 1 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
        The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

Example 2:

Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Explanation:

    For i = 0 (l = 1, r = 3, val = 2):
        Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
        The array will become [4, 1, 0, 0].
    For i = 1 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
        The array will become [3, 0, 0, 0], which is not a Zero Array.
'''

class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        n=len(nums)
        sum,k=0,0
        differenceArray=[0]*(n+1)
        # iterate through nums
        for i in range(n):
             # Iterate through queries while current index of nums cannot equal zero
            while(sum+differenceArray[i]<nums[i]):
                k+=1
                  # Zero array isn't formed after all queries are processed
                if(k>len(queries)):
                    return -1
                left,right,val=queries[k-1]
                # process start and end of range
                if (right>=i):
                    differenceArray[max(left, i)] += val
                    differenceArray[right + 1] -= val

            # Update prefix sum at current index
            sum += differenceArray[i]

        return k

# Create an object for the Solution class
solution = Solution()

# Test Case 1
nums1 = [2, 0, 2]
queries1 = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
print(solution.minZeroArray(nums1, queries1))  # Output: 2

# Test Case 2
nums2 = [4, 3, 2, 1]
queries2 = [[1, 3, 2], [0, 2, 1]]
print(solution.minZeroArray(nums2, queries2))  # Output: -1