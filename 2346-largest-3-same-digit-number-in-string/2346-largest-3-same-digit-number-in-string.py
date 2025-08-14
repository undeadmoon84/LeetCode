class Solution:
    def largestGoodInteger(self, num: str) -> str:
        GoodNums = []
        NumsList = list(num)
        for index, value in enumerate(NumsList[:-2]):
            if value == NumsList[index+2] == NumsList[index+1]:
                GoodNums.append(int(value))
        if not GoodNums:
            return ''
        elif GoodNums:
            return str(max(GoodNums)) * 3