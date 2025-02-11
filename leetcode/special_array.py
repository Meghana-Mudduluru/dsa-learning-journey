'''An array is considered special if every pair of its
 adjacent elements contains two numbers with different parity. '''

class Solution(object):
    def isArraySpecial(self, nums):
        for i in range(0,len(nums)-1):
            if nums[i] %2 == nums[i+1] %2 :
                return False
        return True
s=Solution()
result=s.isArraySpecial([1])
result2=s.isArraySpecial([2,1,4])
result3=s.isArraySpecial([4,3,1,6])
print(result)
print(result2)
print(result3)