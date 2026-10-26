class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dicts.keys():
                return sorted([dicts[comp], i])
            dicts[nums[i]] = i
            