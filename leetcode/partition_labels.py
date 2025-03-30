'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]

Constraints:

    1 <= s.length <= 500
    s consists of lowercase English letters.
'''

from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Store the last occurrence of each character in a dictionary
        last_index = {char: idx for idx, char in enumerate(s)}

        # Step 2: Initialize pointers for partitioning
        partitions = []
        start, end = 0, 0

        # Step 3: Iterate through the string to determine partitions
        for i, char in enumerate(s):
            end = max(end, last_index[char])  # Update the end index of current partition

            # If the current index reaches the end index of a partition
            if i == end:
                partitions.append(end - start + 1)  # Add partition size to result
                start = i + 1  # Move start to next segment

        return partitions

# Create an object of Solution class and test the function
solution = Solution()
example_string = "ababcbacadefegdehijhklij"
result = solution.partitionLabels(example_string)
print(result)