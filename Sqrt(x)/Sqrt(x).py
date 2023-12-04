from math import floor, sqrt

class Solution:
    def mySqrt(self, x: int) -> int:
        return floor(sqrt(x))
    
sol = Solution.mySqrt(16)
print(sol)