class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                sum = nums[l] + nums[r]
                if sum == target:
                    return [l,r]
        return[l,r]