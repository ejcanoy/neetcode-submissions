class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

            

        swap(0,len(nums) - 1)
        swap(0, k % len(nums) - 1)
        swap(k % len(nums), len(nums) - 1)


        