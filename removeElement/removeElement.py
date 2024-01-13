class Solution:
    def removeElement(self, nums: list[int], val: int) -> list(int):
            self.nums = nums
            self.val = val
            original_lenth = len(nums)
            k = []
            for i in nums:
                    if i != val:  
                        k.append(i)
            new_length = len(k)
            # for i in range(original_lenth - new_length):
            #       k.append(0)  
            return k




if __name__ == "__main__":
    # nums = [3,2,2,3]
    # val = 3
    nums = [3,2,2,3]
    val = 2
    print(Solution().removeElement(nums, val))

# py .\removeElement.py