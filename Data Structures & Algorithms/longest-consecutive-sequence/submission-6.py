import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        count = 0
        for num in nums:
            if num - 1 not in seq:
                cur_num = num
                cur_count = 1
                while cur_num + 1 in seq:
                    cur_count += 1
                    cur_num += 1
            
                count = max(cur_count, count)
        
        return count