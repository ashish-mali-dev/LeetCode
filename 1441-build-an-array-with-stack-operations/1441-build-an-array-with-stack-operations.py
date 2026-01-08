class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        c=0

        for i in range(1,n+1):
            res.append("Push")

            if i == target[c]:
                c+=1
                if c==len(target):
                    break
            else:
                res.append("Pop")
        return res
