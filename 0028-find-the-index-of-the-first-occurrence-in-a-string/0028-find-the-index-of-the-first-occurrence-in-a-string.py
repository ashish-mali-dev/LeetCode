class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(needle)>len(haystack)):
            return -1
        
        m=len(needle)
        n=len(haystack)

        for i in range(n-m+1):
            j=0

            while j<m:
                if(haystack[i+j]!=needle[j]):
                    break
                j+=1
            if j==m:
                return i
        return -1



