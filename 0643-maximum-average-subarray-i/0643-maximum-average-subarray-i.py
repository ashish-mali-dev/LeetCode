class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        if n < k:
            return 0.0

        # initialize window [0 .. k-1]
        low = 0
        high = k - 1

        window_sum = 0
        for i in range(low, high + 1):
            window_sum += nums[i]

        max_sum = window_sum

        # slide window to the right
        while high + 1 < n:
            # remove outgoing
            window_sum -= nums[low]
            low += 1

            # expand incoming
            high += 1
            window_sum += nums[high]

            # update best
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k
