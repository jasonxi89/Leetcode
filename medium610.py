class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    610. 两数和 - 差等于目标值
    给定一个整数数组，找到两个数的 差 等于目标值。index1必须小于index2。注意返回的index1和index2不是 0-based。

    样例
    给定的数组为 [2,7,15,24]，目标值为 5，返回 [1,2] (7 - 2 = 5)

    注意事项
    保证只有一个答案。
    """
    def twoSum7(self, nums, target):
        # write your code here
        dict ={}
        for i in range(len(nums)):
            if dict.get(target + nums[i]) != None :
                return [dict.get(target + nums[i]),i]
            if dict.get(nums[i]-target) != None:
                return [dict.get(nums[i]-target), i]
            else:
                dict[nums[i]] = i


