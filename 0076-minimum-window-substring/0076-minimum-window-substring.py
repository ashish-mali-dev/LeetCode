class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
                return ""

        need = Counter(t)                 # required counts Counter({'A': 1, 'B': 1, 'C': 1})
        window = defaultdict(int)         # current window counts
        required = len(need)              # how many distinct chars must match
        formed = 0                        # how many distinct chars currently satisfy need

        low = 0
        best_len = float('inf')
        best_l = 0

        for high in range(len(s)):
            window[s[high]] += 1
            if s[high] in need and window[s[high]] == need[s[high]]:
                formed += 1

            # When valid, contract from left to find smaller valid windows
            while low <= high and formed == required:
                # update best
                if high - low + 1 < best_len:
                    best_len = high - low + 1
                    best_l = low

                # pop left char and update formed if necessary
                left_char = s[low]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                low += 1

        return "" if best_len == float('inf') else s[best_l:best_l + best_len]
