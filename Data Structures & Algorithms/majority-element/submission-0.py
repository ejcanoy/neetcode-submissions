class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = nums[0]
        count = 0
        for num in nums:
            if num == n:
                count += 1
            else:
                count -= 1
                if count == 0:
                    n = num
                    count = 1
        
        return n