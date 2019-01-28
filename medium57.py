class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

    样例
    如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：

    (-1, 0, 1)

    (-1, -1, 2)

    注意事项
    在三元组(a, b, c)，要求a <= b <= c。

    结果不能包含重复的三元组。
    """
    # 暴力开搞法
    # def threeSum(self, numbers):
    #     # write your code here
    #
    #     ret = set()
    #     if len(numbers) < 3:
    #         return None
    #     for l in range(0, len(numbers) - 2):
    #         for m in range(l + 1, len(numbers) - 1):
    #             for r in range(m + 1, len(numbers)):
    #                 if numbers[r] + numbers[m] + numbers[l] == 0:
    #                     ret.update([numbers[l], numbers[m], numbers[r]])
    #     return list(ret)



    # 小机智方法，dic去重，算 a = - b - c
    # def threeSum(self, nums):
    #     nums.sort()
    #     results = []
    #     length = len(nums)
    #     for i in range(0, length - 2):
    #         if i and nums[i] == nums[i - 1]:
    #             continue
    #         target = -nums[i]
    #         left, right = i + 1, length - 1
    #         while left < right:
    #             if nums[left] + nums[right] == target:
    #                 results.append([nums[i], nums[left], nums[right]])
    #                 right -= 1
    #                 left += 1
    #                 while left < right and nums[left] == nums[left - 1]:
    #                     left += 1
    #                 while left < right and nums[right] == nums[right + 1]:
    #                     right -= 1
    #             elif nums[left] + nums[right] > target:
    #                 right -= 1
    #             else:
    #                 left += 1
    #     return results

if __name__ =="__main__":
    print(Solution.threeSum(Solution,[-1,1,0]))