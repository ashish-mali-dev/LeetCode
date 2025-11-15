class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)*2
        for i in range(len(nums)):
            ans[i] = nums[i]
            print(len(nums)//2+i)
            ans[len(nums)+i] = nums[i]
        return ans