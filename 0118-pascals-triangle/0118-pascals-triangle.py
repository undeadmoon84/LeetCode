class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for i in range(numRows):
            if i == 0:
                lst.append([1])
            else:
                prev = lst[i - 1]
                row = [1]
                for j in range(len(prev) -1):
                    row.append(prev[j] + prev[j + 1])
                row.append(1)
                lst.append(row)
        return lst