class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tdict = {}
        sdict = {}
        if len(t) != len(s):
            return False
        else:
            for i in t:
                if i in tdict:
                    tdict[i] += 1
                else:
                    tdict[i] = 1
            for j in s:
                if j in sdict:
                    sdict[j] += 1
                else:
                    sdict[j] = 1
            if sdict == tdict:
                return True
            else:
                return False