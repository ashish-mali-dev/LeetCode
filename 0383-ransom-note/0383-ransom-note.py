class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={} # same as anagram

        for ch in ransomNote:
            freq[ch] = freq.get(ch,0)+1
        
        for ch in magazine:
            if ch in freq:
                freq[ch]-=1
                if freq[ch]==0:
                    del freq[ch]
        return len(freq)==0