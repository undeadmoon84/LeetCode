class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dict = {}
        # for i in nums:
        #     if i in dict:
        #         return True
        #     else:
        #         dict[i] = 1
        # return False
        if len(nums) > len(set(nums)):
            return True
        return False