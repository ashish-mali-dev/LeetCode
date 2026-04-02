class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res=""
        chars={}

        char=0
        for k in key:
            if k in chars or k==" ":
                continue
            chars[k]=char
            char+=1
            
        for m in message:
            if m ==" ":
                res+=" "
            else:
                res+=chr(97+chars[m])

        return res