class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left = [1] * len(nums)
        # right = [1] * len(nums)

        # for i in range(1,len(left)):
        #     left[i] = nums[i] * nums[i - 1]

        # for i in range(len(right) - 2, -1, -1):
        #     print(nums[i], nums[i + 1])
        #     right[i] = nums[i] * nums[i + 1]

        # print(left,right)
        output = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output
