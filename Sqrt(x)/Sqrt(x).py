from math import floor, sqrt

class Solution():
    def __init__(self, x: int) -> None:
        self.num = x

    def mySqrt(self) -> int:
        return floor(sqrt(self.num))

number1 = Solution(81)
sqrt1 = number1.mySqrt()
print(f"The square root of {number1.num} is {sqrt1}.")

# py .\sqrt.py