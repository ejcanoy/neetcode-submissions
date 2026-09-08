class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            cur = (r - l) // 2 + l
            if nums[cur] == target:
                return cur
            elif nums[cur] > target:
                r = cur - 1
            else:
                l = cur + 1        
        return -1