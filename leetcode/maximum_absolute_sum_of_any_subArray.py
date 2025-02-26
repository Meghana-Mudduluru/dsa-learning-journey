class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)

        return max_prefix_sum - min_prefix_sum

# Create an object of the Solution class
sol = Solution()

# Example input
nums = [1, -3, 2, 3, -4]
nums1 = [2,-5,1,-4,3,-2]
# Call the method and print the result
result = sol.maxAbsoluteSum(nums)
print(result)
result1 = sol.maxAbsoluteSum(nums1)
print(result1)
