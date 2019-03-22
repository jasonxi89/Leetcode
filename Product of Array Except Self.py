class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            out.append(p)
            p *=nums[i]
        p = 1
        for i in range(n-1, -1, -1)
            output[i] *= p
            p *= nums[i]
        return output
#先求这个数左边的数组乘积
#再求这个数右边的数组乘积
# 原数组:{1 2 3 4}
# 左边乘积: {1, 1, 2, 6}
# 右边乘积: {24, 12, 4, 1}
# 输出{24, 12, 8, 6}
