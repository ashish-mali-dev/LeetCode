class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        low=0
        high=len(p)
        window=defaultdict(int)
        need=defaultdict(int)
        ans=[]

        if high > len(s):
            return []   

        for i in range(high):
            need[p[i]]+=1
        
        for i in range(high):
            window[s[i]]+=1

        if(window==need):
            ans.append(0)

        for i in range(high,len(s)):
           out_char = s[i - high]
            # remove outgoing
           window[out_char] -= 1
           if window[out_char] == 0:
               del window[out_char]

            # add incoming
           window[s[i]] += 1

           if window == need:
                ans.append(i - high + 1)
        return ans