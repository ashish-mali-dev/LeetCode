class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {},{} # for s to be isomorphic to t, t has to be isomorphic to s as well, so basically both mappings should hold true

        for i in range(len(s)): # both will have same length as per constraint
            c1, c2 = s[i], t[i]

            if((c1 in mapST and mapST[c1]!=c2) or (c2 in mapTS and mapTS[c2]!=c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1
        return True