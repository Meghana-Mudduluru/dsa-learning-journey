class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        result = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(index: int) -> bool:
            if index == len(result):
                return True
            if result[index] != 0:
                return backtrack(index + 1)

            for num in range(n, 0, -1):
                if used[num]:
                    continue

                used[num] = True
                result[index] = num

                if num == 1 or (index + num < len(result) and result[index + num] == 0):
                    if num > 1:
                        result[index + num] = num
                    if backtrack(index + 1):
                        return True
                    if num > 1:
                        result[index + num] = 0

                result[index] = 0
                used[num] = False

            return False

        backtrack(0)
        return result

sol=Solution()
print(sol. constructDistancedSequence(3))
print(sol. constructDistancedSequence(5))