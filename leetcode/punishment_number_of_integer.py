class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s, target, index=0, cur_sum=0):
            if (index == len(s)):
                return cur_sum == target

            for i in range(index, len(s)):
                part = int(s[index:i + 1])
                if (can_partition(s, target, i + 1, cur_sum + part)):
                    return True
            return False

        total = 0

        for i in range(1, n + 1):
            sqr_str = str(i * i)
            if (can_partition(sqr_str, i)):
                total = total + (i * i)

        return total

n = 10
print(Solution().punishmentNumber(n))  # Output: 182

n = 37
print(Solution().punishmentNumber(n))  # Output: 1478