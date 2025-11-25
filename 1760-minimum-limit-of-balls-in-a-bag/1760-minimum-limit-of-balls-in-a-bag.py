from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)

        def ok(X):
            ops = 0
            for n in nums:
                ops += (n - 1) // X
                if ops > maxOperations:
                    return False
            return True

        while low < high:
            mid = low + (high - low) // 2
            if ok(mid):
                high = mid          # feasible → try smaller max size
            else:
                low = mid + 1       # too small → need larger size

        return low
