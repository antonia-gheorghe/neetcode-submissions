class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits)-1

        if digits[-1] == 9:   # last digit is 9 
            while digits[i] == 9:  # while still 9 
                digits[i] = 0      # make it 0
                i -=1 

            if i == -1:
                return [1] + digits  # if all were 9 add a 1 to the front 
            else:
                digits[i] += 1       # else just ass 1 tot first digit 
                return digits
        else:                        # last digit not 9
            digits[-1] +=1           # just add 1 to last one 
            return digits
        