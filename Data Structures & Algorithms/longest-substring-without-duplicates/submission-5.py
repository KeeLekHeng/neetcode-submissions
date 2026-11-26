class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        length = 0
        hashset = set()
        l = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            
            hashset.add(s[r])
            length = r - l + 1
            longest = max(longest, length)
        return longest







#abacdefgba