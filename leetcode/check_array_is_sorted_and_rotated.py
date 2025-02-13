class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if(nums[i] > nums[i + 1]):
                count = count + 1
                if (count > 1):
                    return False
            if(count==1 and nums[0]<nums[-1]):
                return False
        return True

sol=Solution()
result=sol.check([3, 4, 5, 1, 2])
result2=sol.check([2, 1, 3, 4])
print(result)
print(result2)
print(sol.check([1,2,3]))