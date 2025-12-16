class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            n = abs(nums[i])
            nums[n-1] = -(abs(nums[n-1]))

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)

        return res

# Iterate through the array. For each number n, take its absolute value and mark the index n-1 as negative.
# This step effectively marks that the number n exists in the array.
# After processing all numbers, iterate through the array again.
# If an index i is positive, then i+1 was never marked, so it’s missing.
# Collect all such missing numbers and return them.