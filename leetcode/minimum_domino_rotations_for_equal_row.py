'''
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.



Example 1:

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.

'''

from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res = self.getRotation(tops, bottoms, tops[0])
        if bottoms[0] != tops[0]:
            res = min(res, self.getRotation(tops, bottoms, bottoms[0]))
        return -1 if res == float('inf') else res

    def getRotation(self, tops: List[int], bottoms: List[int], target: int) -> int:
        rotate_top = rotate_bottom = 0
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return float('inf')
            if tops[i] != target:
                rotate_top += 1
            if bottoms[i] != target:
                rotate_bottom += 1
        return min(rotate_top, rotate_bottom)


sol = Solution()
print(sol.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))  # Output should be 2
