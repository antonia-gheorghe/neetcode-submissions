class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # ^ (xor) -> compares two numbers bit by bit.  bit is 1 if the two bits are different and 0 if they’re the same.
        # a ^ a = 0 (000000000)
        # a ^ 0 = a 
        # a ^ b = b ^ a

        result = 0

        for num in nums:
            result ^= num
        
        return result 
        