import string 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        counts = {ch: 0 for ch in string.ascii_lowercase} 

        for i in range(len(s)):
            counts[s[i]] +=1
            counts[t[i]] -=1
        
        for i in counts.keys():
            if counts[i] != 0:
                return False

        return True

        


        