class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in values:
                return [i, values[complement]]
            values[nums[i]] = i