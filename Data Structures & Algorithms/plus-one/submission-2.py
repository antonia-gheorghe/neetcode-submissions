class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits)-1

        if digits[-1] == 9: 
            while digits[i] == 9:
                digits[i] = 0
                i -=1 

            if i == -1:
                return [1] + digits
            else:
                digits[i] += 1
                return digits
        else:
            digits[-1] +=1
            return digits
        