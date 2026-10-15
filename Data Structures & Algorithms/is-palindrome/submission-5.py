import string
class Solution:
    def isPalindrome(self, s: str) -> bool:

        parsed = ""

        for ch in s:
            if ch.isalnum():
                parsed += ch.lower()

        for i in range(len(parsed)//2):
            if parsed[i]!=parsed[len(parsed)-i-1]:
                return False 
        
        return True

        