class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    533. 两数和的最接近值
    找到两个数字使得他们和最接近target

    样例
    nums = [-1, 2, 1, -4],target = 4.

    最接近值为 1

    nums

    挑战
    Do it in O(nlogn) time complexity.
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        # 本来想sort,但是感觉挺傻逼？
        nums.sort()
        i, j = 0, len(nums) - 1

        diff = float('inf')
        while i < j:
            if nums[i] + nums[j] < target:
                diff = min(diff, target - nums[i] - nums[j])
                i += 1
            else:
                diff = min(diff, nums[i] + nums[j] - target)
                j -= 1

        return diff
