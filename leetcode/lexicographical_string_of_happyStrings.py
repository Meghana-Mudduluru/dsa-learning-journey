class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        stringsStack=[""]
        indexInSortedList=0

        total_happy_strings = 3 * (2 ** (n - 1))
        if k > total_happy_strings:
            return ""

        while stringsStack:
            currentString=stringsStack.pop()

            if(len(currentString)==n):
                indexInSortedList+=1
                if indexInSortedList==k:
                    return currentString

            else:
                for char in 'cba':
                    if not currentString or currentString[-1]!=char:
                        stringsStack.append(currentString+char)
        return " "

solution = Solution()
n, k = 1, 4
print(solution.getHappyString(n, k))
solution = Solution()
n, k = 1, 3
print(solution.getHappyString(n, k))
solution = Solution()
n, k = 3,9
print(solution.getHappyString(n, k))