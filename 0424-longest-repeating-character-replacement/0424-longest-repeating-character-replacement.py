class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low=0
        high=0
        res=0
        count=defaultdict(int)
        max_count=0

        for high in range(len(s)):
            count[s[high]]+=1
            max_count = max(max_count, count[s[high]])

            while((high - low + 1) - max_count > k):
                count[s[low]]-=1
                if(count[s[low]]==0):
                    del count[s[low]]
                low+=1
            
            size = high-low+1
            res=max(res,size)
        return res

# window_size = right - left + 1

# max_count = count of the most frequent character seen in this window (or historically max while expanding)

# If window_size - max_count <= k you can replace the other characters to make window all one char. If the condition fails, shrink left.
# We update max_count as we expand: max_count = max(max_count, counts[char]). Yes, max_count can be stale when shrinking — that’s fine. Using the historical max keeps complexity O(n) and correctness intact. The window will shrink when necessary; you never accept an invalid window into the final answer.