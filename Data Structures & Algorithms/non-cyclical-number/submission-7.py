class Solution:
    def sumOfSquares(self, n:int) -> int:
        sum = 0

        for ch in str(n):
            sum += int(ch) ** 2

        return sum 

    def isHappy(self, n: int) -> bool:

        seen = set()

        while True:
            print(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True 
            if n in seen:
                return False
            seen.add(n)

        