'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:

    1 <= numRows <= 30

'''

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        row=[1]
        for i in range(numRows):
            result.append(row)
            new_row=[1]
            for j in range(len(row)-1):
                new_row.append(row[j]+row[j+1])
            new_row.append(1)
            row=new_row
        return result

numRows=5
sol=Solution()
print(sol.generate(numRows))