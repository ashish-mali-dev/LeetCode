class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}

        for i in range(len(nums)):
            complement= target - nums[i]

            if complement in temp:
                return [i,temp[complement]]
            else:
                temp[nums[i]] = i
        return[-1,-1]