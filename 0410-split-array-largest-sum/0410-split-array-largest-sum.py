class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = low + (high - low) // 2

            if self.can_split(nums, k, mid):
                high = mid
            else:
                low = mid + 1

        return low

    def can_split(self, nums, k, mid):
        count = 1
        curr = 0

        for num in nums:
            if curr + num > mid:
                count += 1
                curr = num
                if count > k:
                    return False
            else:
                curr += num

        return True