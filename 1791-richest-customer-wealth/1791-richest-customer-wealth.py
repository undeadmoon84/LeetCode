class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = max(sum(i) for i in accounts)
        return max_sum
        