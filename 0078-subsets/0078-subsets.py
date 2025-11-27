from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if i == len(nums):
                res.append(path[:])     # copy current subset
                return

            # choose nums[i]
            path.append(nums[i])
            dfs(i + 1)

            # backtrack
            path.pop()

            # skip nums[i]
            dfs(i + 1)

        dfs(0)
        return res
