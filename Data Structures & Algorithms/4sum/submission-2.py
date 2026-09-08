class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        end = len(nums)
        i = 0
        nums = sorted(nums)
        res = []
        while i < end - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            while j < end - 2:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                l = j + 1
                r = end - 1
                while l < r:
                    cur_total = nums[i] + nums[j] + nums[l] + nums[r]
                    if cur_total == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                    if cur_total > target:
                        r -= 1
                    else:
                        l += 1
                j += 1
            i += 1
        return res