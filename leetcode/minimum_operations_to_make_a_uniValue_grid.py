'''
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.



Example 1:

Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following:
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

Example 2:

Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.

Example 3:

Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.

'''

class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        # Flatten the grid into a 1D list
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)

        # Check if all elements have the same remainder when divided by x
        first_remainder = nums[0] % x
        for num in nums:
            current_remainder = num % x
            if current_remainder != first_remainder:
                return -1  # Not possible to make all values equal

        # Sort the list to find the median
        nums.sort()
        median = nums[len(nums) // 2]

        # Calculate the total number of operations required
        total_operations = 0
        for num in nums:
            total_operations += abs(num - median) // x

        return total_operations

# Example usage
solution = Solution()
grid = [[2, 4], [6, 8]]
x = 2
result = solution.minOperations(grid, x)
print(result)  # Output: 4
