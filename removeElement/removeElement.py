class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        original_length = len(nums)
        k = 0
        while val in nums:
            for i in range(len(nums)):
                if nums[i] == val:
                    nums.pop(i)
                    k += 1
                    break
        return original_length - k




if __name__ == "__main__":
    # nums = [3,2,2,3]
    # val = 3
    nums = [3,2,2,3]
    val = 2
    print(Solution().removeElement(nums, val))

# py.\removeElement\removeElement.py