class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i,ch in enumerate(s):
            res+=(i+1)*(123-ord(ch))
            print(ord(ch)-71)
            print(ch)
        return res