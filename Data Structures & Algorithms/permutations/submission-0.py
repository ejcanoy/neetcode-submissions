class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, nums):
            if not nums:
                res.append(path)
            for i,n in enumerate(nums):
                dfs(path + [nums[i]], nums[:i] + nums[i + 1:])


        dfs([], nums)
        return res