class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numSet = set()

        res = []

        nums.sort()

        for i, a in enumerate(nums):
            #make sure dont reuse same first value
            if i > 0 and a == nums[i-1]:
                continue
            
            #solve the remaining two sum
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    #fast track to reduce l iterations we do not need
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                







