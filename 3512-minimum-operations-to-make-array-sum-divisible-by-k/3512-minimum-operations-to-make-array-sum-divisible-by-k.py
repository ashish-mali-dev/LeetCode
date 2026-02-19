class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        remainder = total%k

        if remainder==0:
            return 0
        
        return remainder