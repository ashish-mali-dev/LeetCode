class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        s=list(s) #Strings are immutable
        high=k-1
        for i in range(k//2):
            temp=s[i]
            s[i]=s[high]
            s[high]=temp
            high-=1
        return "".join(s)

