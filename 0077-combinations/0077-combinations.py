class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        path=[]

        def dfs(i:int):
            if len(path)==k:
                res.append(path[:])
                return
            
            for x in range(i,n+1):
                path.append(x)
                dfs(x+1)
                path.pop()

        dfs(1)
        return res

# Think of numbers [1, 2, 3, 4].
# You need all subsets of fixed size k.

# So it’s still include/exclude recursion, but you stop when the current path has size k.

# This saves half the branching because we prune early.