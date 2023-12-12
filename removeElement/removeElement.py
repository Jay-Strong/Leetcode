class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
            self.nums = nums
            self.val = val
            nums.remove(val)

            return nums




if __name__ == "__main__":

    arr = [3,2,2,3]
    val = 3
    print(Solution().removeElement(arr, val))

# py .\removeElement\removeElement.py