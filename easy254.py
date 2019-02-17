class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    254. 丢鸡蛋
    楼有n层高，鸡蛋若从k层或以上扔，就会碎。从k层以下扔，就不会碎。

    现在给两个鸡蛋，用最少的扔的次数找到k。返回最坏情况下次数。

    样例
    给出 n = 10, 返回 4.
    给出 n = 100, 返回14.

    说明
    对于n=10， 一种找k的初级方法是从1、2...k层不断找。但最坏情况下要扔10次。

    注意有两个鸡蛋可以使用，所以可以从4、7、9层扔。这样最坏就只需要4次(例如k=6时)。

    有个公式 n(n+1)/2 > 100

    最多次数和第一次丢的楼层数一样
    """
    def dropEggs(self, n):
        # write your code here
        import math
        x = int(math.sqrt(n * 2))
        while x * (x + 1) / 2 < n:
            x += 1
        return x