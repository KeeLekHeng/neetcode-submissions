class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ("".join(s.split())).lower()

        non = "!@,.?':"
        for char in non:
            s = s.replace(char, "")

        for i in range(len(s)):
            j = len(s) - i - 1

            if i > j:
                break
                
            if s[i] != s[j]:
                return False
        return True
        

        
        
            

        