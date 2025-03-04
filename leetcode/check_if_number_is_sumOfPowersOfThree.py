class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:  # If we see a '2' in base-3, it's not possible
                return False
            n //= 3  # Move to the next digit in base-3
        return True

# Create an object of the Solution class
sol = Solution()

# Test cases
print(sol.checkPowersOfThree(12))  # True
print(sol.checkPowersOfThree(91))  # True
print(sol.checkPowersOfThree(21))  # False
