class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        n = len(nums)
        d = {}
        for i in range(n):
            if nums[i] in d.keys():
                if abs(d[nums[i]] - i) <= k:
                    return True
                else:
                    d[nums[i]] = i
            else:
                d[nums[i]] = i
        return False