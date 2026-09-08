class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        if len(nums) < 3:
            return [-1]

        l = 0
        r = len(nums) - 1
        res = []
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r: 
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

            i += 1
        
        return res