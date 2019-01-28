class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    608. 两数和 II-输入已排序的数组
    给定一个已经 按升序排列 的数组，找到两个数使他们加起来的和等于特定数。
    函数应该返回这两个数的下标，index1必须小于index2。注意返回的值不是 0-based。

    样例
    给定数组为 [2,7,11,15] ，target = 9
    返回 [1,2]

    注意事项
    你可以假设每个输入刚好只有一个答案
    """
    def twoSum(self, nums, target):
        # write your code here
        l, r = 0 , len(nums) -1
        while  l < r:
            if nums[l] + nums[r] == target:
                return [l +1, r + 1]
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        pass
