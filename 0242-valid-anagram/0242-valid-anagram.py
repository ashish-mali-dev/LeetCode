class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_map = {}

        for ch in s:
            frequency_map[ch] = frequency_map.get(ch,0)+1

        for ch in t:
            if ch in frequency_map:
                frequency_map[ch]-=1
                if frequency_map[ch] ==0:
                    del frequency_map[ch]
            else:
                return False
        return len(frequency_map)==0