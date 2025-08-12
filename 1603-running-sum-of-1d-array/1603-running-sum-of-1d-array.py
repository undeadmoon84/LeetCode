class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return[ sum(nums[:index+1])for index, num in enumerate(nums) ]
