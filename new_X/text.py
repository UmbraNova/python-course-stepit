class Solution(object):
    def twoSum(self, nums, target):
        if nums[0] + nums[1] == target:
            return (0, 1)
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                return (i, nums[i+1:].index(target-nums[i])+i+1)

        # l = len(nums)
        # return [(i, j+1) for i in range(l) for j in range(i, l-1) if nums[i] + nums[j+1] == target][0]

        # dct = dict()
        # for i in range(len(nums)):
        #     if nums[i] in dct:
        #         return [i, dct[nums[i]]]
        #     else:
        #         dct[target-nums[i]] = i

        # for i in range(len(nums)-1):                   
        #     for j in range(i+1,len(nums)):         
        #         if nums[i]+nums[j] == target:      
        #             return i, j