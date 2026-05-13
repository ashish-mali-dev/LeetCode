class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=0

        for i in range(len(accounts)):
            amt=0
            for acc in accounts[i]:
                amt+=acc
            res=max(res,amt)
        return res
