class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        whatever = {}
        for i, v in enumerate(nums):
            diff = target - v

            if diff in whatever:
                return [whatever[diff], i]

            whatever[v] = i