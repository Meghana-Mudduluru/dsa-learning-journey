class Solution(object):
    def maximumSum(self, nums):
        digit_sums = {}
        max_sum = -1

        for num in nums:
            digit_sum = 0
            temp = num
            while temp:
                n = temp % 10
                digit_sum += n
                temp = temp // 10

            if digit_sum in digit_sums:
                max_sum = max(max_sum, num + digit_sums[digit_sum])

            if digit_sum not in digit_sums or num > digit_sums[digit_sum]:
                digit_sums[digit_sum] = num
        return max_sum


p = Solution()
print(p.maximumSum([18,43,36,13,7]))
print(p.maximumSum([10, 12, 19, 14]))
