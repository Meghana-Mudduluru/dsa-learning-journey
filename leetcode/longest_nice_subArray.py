'''
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.



Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

Example 2:

Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.

'''


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:

        left = 0  # Left pointer of the sliding window
        bitmask = 0  # Stores the bitwise OR of the current subarray
        max_length = 0  # Stores the maximum length of a nice subarray

        for right in range(len(nums)):
            # While the AND operation is not 0, shrink the window from the left
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]  # Remove the leftmost element from the bitmask
                left += 1

            # Include the new element in the bitmask
            bitmask |= nums[right]

            # Update max_length
            max_length = max(max_length, right - left + 1)

        return max_length

# Create an instance of the Solution class
sol = Solution()

# Example test cases
nums1 = [1, 3, 8, 48, 10]
nums2 = [3, 1, 5, 11, 13]

# Call the method and print results
print(sol.longestNiceSubarray(nums1))  # Output: 3
print(sol.longestNiceSubarray(nums2))  # Output: 1