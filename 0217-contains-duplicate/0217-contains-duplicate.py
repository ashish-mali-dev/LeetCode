class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        distinct_values = set()
    
        for num in nums:
            if num in distinct_values:
                return True
            distinct_values.add(num)

        return False