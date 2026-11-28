class Solution:
    def findMin(self, nums: List[int]) -> int:
        lowest = max(nums)
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r) // 2
            lowest = min(lowest, nums[middle])
            
            if nums[middle] >= nums[l]:
                lowest = min(nums[l], lowest)
                l = middle + 1
            else:
                r = middle - 1
        return lowest




# 1, 2, 3, 4, 5, 6
# 5, 6, 1, 2, 3, 4