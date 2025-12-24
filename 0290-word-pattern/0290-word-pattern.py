class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        mapWP, mapPW = {},{}

        if len(words)!= len(pattern):
            return False
        
        for i in range(len(words)):
            c1, c2 = words[i], pattern[i]

            if((c1 in mapWP and mapWP[c1]!=c2) or (c2 in mapPW and mapPW[c2]!=c1)):
                return False
            
            mapWP[c1] = c2
            mapPW[c2] = c1

        return True