class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    587. 两数之和 - 不同组成
        给一整数数组, 找到数组中有多少组 不同的元素对 有相同的和, 且和为给出的 target 值, 返回对数.

        样例
        给一数组 nums = [1,1,2,45,46,46], target = 47, 返回 2
        1 + 46 = 47
        2 + 45 = 47
    """

    def twoSum6(self, nums, target):
        # write your code here
        # dic的值为是否被重复用过：T是用过，F是没用过

        dict = {}
        count = 0
        for num in nums:
            # 如果target-num在字典里，而且没用过 | 如果target-num在字典里，且用过 |如果target-num不在字典里[1,3,3,1,1,1,3,3,3,]
            if target - num in dict:
                if (dict[target - num] == False):
                    count += 1
                    #2个都要写，因为2个胡子都用过。
                    dict[target - num] = True
                    dict[num] = True
                else:
                    dict[num] = True
            else:
                dict[num] = False

        return count

