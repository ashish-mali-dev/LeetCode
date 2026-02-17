class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        low = 0
        count_0 = 0
        count_1 = 0
        result = 0

        for high in range(len(s)):
            # Expand window
            if s[high] == '0':
                count_0 += 1
            else:
                count_1 += 1

            # If invalid (both exceed k), shrink window
            while count_0 > k and count_1 > k:
                if s[low] == '0':
                    count_0 -= 1
                else:
                    count_1 -= 1
                low += 1

            # Add valid substrings ending at high
            result += (high - low + 1)

        return result
