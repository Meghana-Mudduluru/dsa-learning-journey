class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")

        return "".join(ans)

sol=Solution()
print(sol.findDifferentBinaryString(["00","01"]))
print(sol.findDifferentBinaryString(["111","011","001"]))
print(sol.findDifferentBinaryString(["01","10"]))