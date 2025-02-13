import heapq


class Solution(object):
    def minOperations(self, nums, k):

        heapq.heapify(nums) # turns the list into min-heap

        count = 0
        while nums[0] < k: # continues if the num is less than k
            small = heapq.heappop(nums) # take smallest num from array
            small2 = heapq.heappop(nums) # take second small number from the array
            op = (small * 2) + small2
            heapq.heappush(nums, op) # add new num back to array
            count = count + 1
        return count

sol = Solution()
print(sol.minOperations([2, 11, 10, 1, 3], 10))
print(sol.minOperations([1, 1, 2, 4, 9], 20))


