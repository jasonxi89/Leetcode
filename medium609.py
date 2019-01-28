class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    609. 两数和-小于或等于目标值
        给定一个整数数组，找出这个数组中有多少对的和是小于或等于目标值。返回对数。

        样例
        给定数组为 [2,7,11,15]，目标值为 24
        返回 5。
        2+7<24
        2+11<24
        2+15<24
        7+11<24
        7+15<24
    """
    def twoSum5(self, nums, target):
        # write your code here

        nums.sort()
        count = 0
        for l in range(0,len(nums)-1):
            # print(l)
            for w in range(len(nums)-1,l,-1):
                if nums[l] + nums[w] <= target:
                    print()
                    count += w - l 
        return count

