class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set()
        for num in set(nums1):
            if num in set(nums2):
                res.add(num)
        return list(res)
