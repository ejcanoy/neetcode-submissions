from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        
        result = []
        for val in hm:
            if hm[val] > len(nums) / 3:
                result.append(val)

        return result