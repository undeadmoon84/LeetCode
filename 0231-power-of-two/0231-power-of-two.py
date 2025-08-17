class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            while n != 1 and n % 1 == 0:
                n /= 2
            if n == 1:
                return True
            else:
                return False