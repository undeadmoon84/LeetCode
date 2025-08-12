class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for i in magazine:
            if i not in dict:
                dict[i] = 1
            elif i in dict:
                dict[i] += 1
        for i in ransomNote:
            if i not in dict:
                return False
            elif i in dict:
                dict[i] -= 1
                if dict[i] < 0:
                    return False
        return True
        

