'''
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

'''


class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:

        meetings.sort()
        merged_intervals = []

        for start, end in meetings:
            if merged_intervals and merged_intervals[-1][1] >= start:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
            else:
                merged_intervals.append([start, end])

        busy_days = sum(end - start + 1 for start, end in merged_intervals)
        return days - busy_days

# Creating an object and testing the function
solution = Solution()
print(solution.countDays(10, [[5,7],[1,3],[9,10]]))  # Output: 2
print(solution.countDays(5, [[2,4],[1,3]]))  # Output: 1
print(solution.countDays(6, [[1,6]]))  # Output: 0

