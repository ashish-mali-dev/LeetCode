class Solution:
    def reverseByType(self, s: str) -> str:
        s=list(s)
        low,high=0,len(s)-1

        while low<high:
            if 97<=ord(s[low])<=122 and 97<=ord(s[high])<=122:
                s[low],s[high] = s[high],s[low]
                low+=1
                high-=1
            elif ord(s[low])<97 or ord(s[low])>122:
                low+=1
            else:
                high-=1
        
        low,high=0,len(s)-1

        while low<high:
            if(ord(s[low])<97 or ord(s[low])>122) and (ord(s[high])<97 or ord(s[high])>122):
                s[low],s[high]=s[high],s[low]
                low+=1
                high-=1
            elif 97<=ord(s[low])<=122:
                low+=1
            else:
                high-=1
        
        return "".join(s)