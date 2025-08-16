class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
            if dict[i] > 1:
                return True
        # for index, value in dict.items():
        #     if value > 1:
        #         return True
        return False
