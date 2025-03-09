class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        count = 0
        max_alt = 1  # Max alternating sequence length
        alt_length = 1  # Current alternating streak

        # Step 1: Find the longest alternating sequence in circular array
        for i in range(1, 2 * n):  # Extend to 2n for wraparound cases
            prev = colors[(i - 1) % n]
            curr = colors[i % n]

            if prev != curr:
                alt_length += 1
            else:
                alt_length = 1  # Reset when adjacent elements are the same

            max_alt = max(max_alt, alt_length)

        # Step 2: Count valid k-length alternating groups
        if max_alt < k:
            return 0  # No k-length alternating groups possible

        # Sliding window approach to count valid segments
        alt_length = 1  # Reset for actual counting
        for i in range(1, n + k - 1):  # Only check `n` valid groups
            if colors[(i - 1) % n] != colors[i % n]:
                alt_length += 1
            else:
                alt_length = 1  # Reset if sequence breaks

            # If we reach length k, count it and move forward
            if alt_length >= k:
                count += 1

        return count

    '''
       n = len(colors)
        count = 0

        # Loop through each possible start index
        for i in range(n):
            # Check if the segment is alternating and within bounds
            is_valid = True
            for j in range(k - 1):
                if colors[(i + j) % n] == colors[(i + j + 1) % n]:
                    is_valid = False
                    break

            # If valid, count it
            if is_valid:
                count += 1

        return count
        '''

sol = Solution()

print(sol.numberOfAlternatingGroups([0,1,0,1,0], 3))  # Output: 3
print(sol.numberOfAlternatingGroups([0,1,0,0,1,0,1], 6))  # Output: 2
print(sol.numberOfAlternatingGroups([1,1,0,1], 4))  # Output: 0
print(sol.numberOfAlternatingGroups([0,1,0,1,0,1,0,1], 4))  # Output: 5
