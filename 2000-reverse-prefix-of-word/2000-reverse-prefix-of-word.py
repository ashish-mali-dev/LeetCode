class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = list(word)
        idx = -1
        
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break
        
        if idx == -1:
            return word
        
        left = 0
        right = idx
        
        while left < right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        
        return "".join(res)