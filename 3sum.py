class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0 :
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append((nums[i],nums[left],nums[right]))
                    left + = 1
                    right - = 1
        return list(set(res))
