class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if (len(s1) != len(s2)):
            return False
        unmatch = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                unmatch.append(i)
                if (len(unmatch) > 2):
                    return False
        if (len(unmatch) == 0):
            return True
        if (len(unmatch) != 2):
            return False
        else:
            i, j = unmatch
            final = (s1[i] == s2[j] and s1[j] == s2[i])
            return final

solution=Solution()
print(solution.areAlmostEqual("bank", "kanb"))   # Output: True
print(solution.areAlmostEqual("attack", "defend")) # Output: False
print(solution.areAlmostEqual("kelb", "kelb"))   # Output: True
