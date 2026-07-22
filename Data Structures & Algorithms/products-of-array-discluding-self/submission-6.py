class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        mul=1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    mul*=nums[j]
            res.append(mul)
            mul=1
        return res