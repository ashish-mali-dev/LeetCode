class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res={}

        for s in s1.split():
            if s not in res:
                res[s]=1
            else:
                res[s]+=1

        for s in s2.split():
            if s not in res:
                res[s]=1
            else:
                res[s]+=1
        
        return [k for k, v in res.items() if v == 1]