class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_seen = -1
        res=[-1]*len(arr)

        for i in range(len(arr)-1,-1,-1):
            res[i] = max_seen
            max_seen=max(max_seen, arr[i])
        
        return res