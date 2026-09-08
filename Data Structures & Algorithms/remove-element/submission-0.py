class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lp = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
            else:
                nums[lp] = nums[i]
                lp += 1
            
        return len(nums) - count