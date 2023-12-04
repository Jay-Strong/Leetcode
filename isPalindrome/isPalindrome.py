class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range (len(x)//2):
            if x[i] != x[-1 - i]:
                return False
        return True
    
solution1 = Solution().isPalindrome(1232)
print(solution1)
