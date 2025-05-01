class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        left = 0
        right = k-1
        n = len(nums)
        summ = sum(nums[left:right+1])
        average = summ/k
        while (right < n-1):
            summ -= nums[left]
            left += 1
            right += 1
            summ += nums[right]
            average = max(average, summ/k)
        return round(average, 5)