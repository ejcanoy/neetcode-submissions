class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(i, sum, path):
            if sum == target:
                res.append(path.copy())
                return
            if i >= len(nums) or sum > target:
                return
            path.append(nums[i])
            bt(i, sum + nums[i], path)
            path.pop()
            bt(i + 1, sum, path)

        bt(0, 0, [])
        return res