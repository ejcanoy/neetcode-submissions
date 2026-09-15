class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while nums[fast] and nums[nums[fast]]:
            fast = nums[nums[fast]] 
            slow = nums[slow]
            if fast == slow:
                break
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow