class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        # Track last position of a, b, c
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            # Update last position of current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Add count of valid substrings ending at current position
            # If any character is missing, min will be -1
            # Else min gives leftmost required character position
            total += 1 + min(last_pos)

        return total

# Create an object of the Solution class
solution = Solution()

# Example usage
s = "abcabc"
result = solution.numberOfSubstrings(s)
print(result)  # Output: 10

s1 = "aaacb"
result1 = solution.numberOfSubstrings(s1)
print(result1)  # Output: 3