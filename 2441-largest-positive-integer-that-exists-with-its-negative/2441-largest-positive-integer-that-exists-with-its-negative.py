class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set()
        res=-1

        for num in nums:
            current = -1 * num
            if current in num_set:
                res=max(res,abs(num))
            else:
                num_set.add(num)
        return res