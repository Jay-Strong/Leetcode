class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
            self.nums = nums
            self.val = val
            k = []
            for i in nums:
                 if i != val:
                    k.append(i)
            return k




if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    # nums = [0,1,2,2,3,0,4,2]
    # val = 2
    print(Solution().removeElement(nums, val))

# py .\removeElement.py