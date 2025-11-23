from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)

        def ok(d: int) -> bool:
            total = 0
            for x in nums:
                total += (x + d - 1) // d  # ceil(x/d) without floats
                if total > threshold:      # early exit
                    return False
            return True

        while low < high:
            mid = low + (high - low) // 2
            if ok(mid):
                high = mid          # mid works → try smaller
            else:
                low = mid + 1       # mid too small → need bigger
        return low
