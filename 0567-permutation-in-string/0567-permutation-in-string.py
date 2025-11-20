class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n= len(s1)
        m= len(s2)
        if n > m:
            return False
        
        need=defaultdict(int)
        window=defaultdict(int)

        for i in range(n):
            need[s1[i]]+=1
        
        for i in range(n):
            window[s2[i]]+=1

        if(need==window):
            return True
    
        for i in range(n,m):
            window[s2[i-n]]-=1

            if(window[s2[i-n]]==0):
                del window[s2[i-n]]
            
            window[s2[i]]+=1

            if(window==need):
                return True
        return False