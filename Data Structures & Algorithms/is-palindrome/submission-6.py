class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr= ''
        for char in s:
            #make sure to remove non alphanumeric characters. 
            if char.isalnum():
                newStr += char.lower()
        return newStr == newStr[::-1]