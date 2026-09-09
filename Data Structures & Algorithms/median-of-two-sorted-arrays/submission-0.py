class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combo = sorted(nums1 + nums2)
        if len(combo) % 2 == 1:
            return float(combo[len(combo) // 2])
        else:
            print(len(combo) // 2 - 1, len(combo) // 2)
            return float((combo[len(combo) // 2 - 1] + combo[len(combo) // 2]) / 2)

        print(combo)
        return 1.0