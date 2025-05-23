class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        # Get grid dimensions
        n = len(grid)
        total = n * n

        # Calculate actual sums from grid
        sum_val = sum(num for row in grid for num in row)
        sqr_sum = sum(num * num for row in grid for num in row)

        # Calculate differences from expected sums
        # Expected sum: n(n+1)/2, Expected square sum: n(n+1)(2n+1)/6
        sum_diff = sum_val - total * (total + 1) // 2
        sqr_diff = sqr_sum - total * (total + 1) * (2 * total + 1) // 6

        # Using math: If x is repeated and y is missing
        # sum_diff = x - y
        # sqr_diff = x² - y²
        repeat = (sqr_diff // sum_diff + sum_diff) // 2
        missing = (sqr_diff // sum_diff - sum_diff) // 2

        return [repeat, missing]

# Creating an object of the Solution class
solution = Solution()

# Example usage
grid = [[1, 3], [2, 2]]  # Example input
grid1 = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
result = solution.findMissingAndRepeatedValues(grid)
print(result)  # Output: [Repeated value, Missing value]
result1 = solution.findMissingAndRepeatedValues(grid1)
print(result1)
