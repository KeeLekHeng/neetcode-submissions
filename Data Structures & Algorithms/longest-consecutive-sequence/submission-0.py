class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #we only start a sequence if the n-1 doesnt exist
        hashset = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 in hashset:
                continue
            else:
                start = nums[i]
                lcs = 1
                val = start + 1
                while val in hashset:
                    lcs += 1
                    val += 1
                longest = max(longest, lcs)

        return longest
                




        