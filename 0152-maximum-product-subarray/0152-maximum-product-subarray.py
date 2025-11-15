class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      cur_max = cur_min = best = nums[0]
      for x in nums[1:]:
        if x<0 :
            cur_max, cur_min = cur_min, cur_max

        cur_max = max(x, cur_max*x)
        cur_min = min(x, cur_min*x)

        best = max(best, cur_max)
      return best

# Products flip sign when you multiply by negative numbers. A small negative times a negative can become the biggest positive. Zeros reset everything. So you must track both the best positive product so far and the worst (most negative) product so far at each step — because the worst can become best when multiplied by a negative.

# Key invariants at each index i:

# cur_max = maximum product of subarray ending at i

# cur_min = minimum product of subarray ending at i

# Update both using the current value and the previous cur_max / cur_min.

# When num < 0 you must swap the roles, because multiplying flips sign.