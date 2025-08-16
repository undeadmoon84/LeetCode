class Solution:
    def maximum69Number (self, num: int) -> int:
        lst = []
        for i in str(num):
            lst.append(i)
        for index, value in enumerate(lst):
            if value == "6":
                lst[index] = "9"
                break
        return int(''.join(lst))