class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res=0
        rules={"type":0,"color":1,"name":2}
        for item in items:
            if ruleValue == item[rules[ruleKey]]:
                res+=1
        return res
