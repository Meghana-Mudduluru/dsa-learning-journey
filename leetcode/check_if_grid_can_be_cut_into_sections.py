'''
You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

    (startx, starty): The bottom-left corner of the rectangle.
    (endx, endy): The top-right corner of the rectangle.

Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

    Each of the three resulting sections formed by the cuts contains at least one rectangle.
    Every rectangle belongs to exactly one section.

Return true if such cuts can be made; otherwise, return false.



Example 1:

Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Output: true

Explanation:

The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

Example 2:

Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

Output: true

Explanation:

We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:

Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

Output: false

Explanation:

We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

'''


class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        # Extract sorted unique x and y coordinates where cuts can be made
        x_coords = sorted(set(x for r in rectangles for x in (r[0], r[2])))
        y_coords = sorted(set(y for r in rectangles for y in (r[1], r[3])))

        # Function to check if we can make two valid cuts along a given coordinate axis
        def can_make_cuts(coords, is_x):
            sections = []

            for r in rectangles:
                start, end = (r[0], r[2]) if is_x else (r[1], r[3])
                sections.append((start, end))

            # Sort sections by their starting coordinate
            sections.sort()

            # Try making two cuts that create three valid sections
            count = 0
            last_end = sections[0][1]

            for i in range(1, len(sections)):
                start, end = sections[i]

                if last_end <= start:  # Found a valid gap
                    count += 1
                    if count == 2:  # If we find two valid gaps, return True
                        return True

                last_end = max(last_end, end)  # Update the last_end seen so far

            return False

        # Try making vertical cuts (x-coordinates) or horizontal cuts (y-coordinates)
        return can_make_cuts(x_coords, True) or can_make_cuts(y_coords, False)

# Create an instance of the Solution class
solution = Solution()

# Example input
n = 5
rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

# Call the method and print the result
result = solution.checkValidCuts(n, rectangles)
print(result)  # Output: True