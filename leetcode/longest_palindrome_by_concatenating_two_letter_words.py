'''
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.



Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

'''

from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        used_middle = False

        for word in count:
            rev = word[::-1]
            if word != rev:
                if rev in count:
                    pair_count = min(count[word], count[rev])
                    length += pair_count * 4
                    count[word] -= pair_count
                    count[rev] -= pair_count
            else:
                pair_count = count[word] // 2
                length += pair_count * 4
                count[word] -= pair_count * 2

        for word in count:
            if word[0] == word[1] and count[word] > 0:
                length += 2  # use one word as center
                break

        return length

words = ["lc","cl","gg"]
sol=Solution()
print(sol.longestPalindrome(words))