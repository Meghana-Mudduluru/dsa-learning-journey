class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:

        less = 0
        equal = 0
        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1

        ans = [0] * len(nums)
        lessI = 0
        equalI = less
        greaterI = less + equal
        for i in range(len(nums)):
            num = nums[i]
            if num < pivot:
                ans[lessI] = num
                lessI += 1
            elif num > pivot:
                ans[greaterI] = num
                greaterI += 1
            else:
                ans[equalI] = num
                equalI += 1

        return ans

# Create an object of the Solution class
solution = Solution()

# Example usage
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
nums1 = [-3, 4, 3, 2]
pivot1 = 2
result = solution.pivotArray(nums, pivot)
print(result)  # Output: [9, 5, 3, 10, 10, 12, 14]
result1 = solution.pivotArray(nums1, pivot1)
print(result1)  # Output: [9, 5, 3, 10, 10, 12, 14]
