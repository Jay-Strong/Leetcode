class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range (len (nums)):
            for j in range (i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
solution1 = Solution().twoSum([2,3,4], 7)
print(solution1())


#   py .twoSum\twoSum.py