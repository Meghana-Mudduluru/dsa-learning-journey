class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:

        key_to_sum = {}

        # Copying the array nums1 to the map.
        for nums in nums1:
            key_to_sum[nums[0]] = nums[1]

        # Adding the values to existing keys or create new entries.
        for nums in nums2:
            key_to_sum[nums[0]] = key_to_sum.get(nums[0], 0) + nums[1]

        merged_array = []
        for key, value in sorted(key_to_sum.items()):
            merged_array.append([key, value])

        return merged_array

# Creating an object of the Solution class
solution = Solution()

# Example inputs
nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 3], [3, 4], [4, 2]]

nums3 = [[1,2],[2,3],[4,5]]
nums4 = [[1,4],[3,2],[4,1]]

# Calling the method and printing the result
result = solution.mergeArrays(nums1, nums2)
print(result)
result1 = solution.mergeArrays(nums3, nums4)
print(result1)