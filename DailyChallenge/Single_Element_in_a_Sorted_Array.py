class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        flag = True
        for i, ele in enumerate(nums):
            if not i:
                temps = ele
            else:
                if flag and temps != ele:
                    return temps
                flag = temps != ele
                temps = ele
        return ele
