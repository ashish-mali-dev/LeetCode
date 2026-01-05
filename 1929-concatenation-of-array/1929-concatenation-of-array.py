class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*(2*len(nums))
        mid=len(nums)

        for i,num in enumerate(nums):
            ans[i] = nums[i]
            ans[i+mid] = nums[i]
        
        return ans
        