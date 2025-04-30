class Solution:
    def maximizeSum(self, nums, k: int) -> int:
        summ = max(nums)
        temp = summ
        for i in range(k-1):
            temp += 1
            summ += temp 
        return summ