class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #we only start a sequence if the n-1 doesnt exist
        hashset = set(nums)
        longest = 0

        for num in hashset:
            if (num - 1) not in hashset:
                length = 1
                while (num + length) in hashset:
                    length +=1
                longest = max(length, longest)
                
        return longest
                




        