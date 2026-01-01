class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_map={}

        for ch in s:
            frequency_map[ch] = frequency_map.get(ch,0)+1
        
        for ch in t:
            if ch not in frequency_map:
                return False
            else:
                frequency_map[ch] = frequency_map[ch]-1
                if frequency_map[ch]==0:
                    del frequency_map[ch]
        return len(frequency_map)==0