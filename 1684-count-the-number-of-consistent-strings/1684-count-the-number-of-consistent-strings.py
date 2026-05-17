class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        res=0
        for word in words:
            count=True
            for c in word:
                if c not in allowed:
                    count=False
                    break
            if(count):
                res+=1
        return res
