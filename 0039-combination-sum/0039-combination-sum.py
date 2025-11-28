from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def dfs(i: int, remain: int) -> None:
            if remain == 0:
                res.append(path[:])
                return
            if i == len(candidates) or remain < candidates[i]:
                return

            # choose candidates[i]
            path.append(candidates[i])
            dfs(i, remain - candidates[i])   # stay at i (reuse allowed)
            path.pop()

            # skip candidates[i]
            dfs(i + 1, remain)               # move on

        dfs(0, target)
        return res
