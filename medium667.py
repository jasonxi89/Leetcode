class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    # 写错了，本来以为是求最长回文串的长度，但是并没有说连续，而且包里破解写的稍微有点问题，应该再建一个helper把参数传进去，看上去能好点，
    # 详情请参考medium200
    # def longestPalindromeSubseq(self, s):
    #     # write your code here
    #     if len(s) <= 1:
    #         return len(s)
    #     re = 1
    #     #中轴暴力破解
    #     for mid in range(0,len(s)-1):
    #         longest = 1
    #         leftpointer = mid -1
    #         rightpointer = mid + 1
    #         #2种情况，一种是这个点左右对称，另一种是空白字符左右对称
    #         if leftpointer > -1 and rightpointer < len(s)  and s[leftpointer] == s[rightpointer]:
    #             longest += 1
    #             leftpointer -= 1
    #             rightpointer += 1
    #             while leftpointer > -1 and rightpointer < len(s) and s[leftpointer] == s[rightpointer]:
    #                 longest += 1
    #                 leftpointer -= 1
    #                 rightpointer += 1
    #             if longest > re:
    #                 re = longest
    #         elif rightpointer < len(s) and s[mid] == s[rightpointer]:
    #             rightpointer +=1
    #             longest += 1
    #             while leftpointer > -1 and rightpointer < len(s) and s[leftpointer] == s[rightpointer]:
    #                 longest += 1
    #                 leftpointer -= 1
    #                 rightpointer += 1
    #             if longest > re:
    #                 re = longest
    #     return re

    #领会题目错了3次，第一次是以为连续的子字符串，第二次是当有一个字母出现了7次，我可不可以只用6个，以为可以，其实不可以,那出现了七次可以用么？也不可以！
    # def longestPalindromeSubseq(s):
    #     # write your code here
    #     if not s:
    #         return 0
    #     re = 0
    #     #mark for 1
    #     mark = False
    #     list = [0 for _ in range(26)]
    #     for w in s:
    #         list[ord(w) - 97] += 1
    #     for num in list:
    #         if num % 2 == 0:
    #             re += num
    #         elif num == 1:
    #             mark = True
    #
    #     if mark:
    #         re +=1
    #
    #     print(list)
    #     return max(re,1)
    #
    #第四次领会错误，abbbcb是B因为可以忽略c,同理cbdxdvbc是因为可以忽略很多，https://www.youtube.com/watch?v=_nCsPn7_OgI看了这个视频，学会DP的思想
    def longestPalindromeSubseq(s):
        # write your code here
        if not s:
            return 0
        n = len(s)
        is_pa = [[0] * n for w in range(n)]
        for i in range( n - 1, -1, -1):
            is_pa[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    is_pa[i][j] = is_pa[i+1][j-1] +2
                else:
                    is_pa[i][j] = max(is_pa[i+1][j],is_pa[i][j-1])
        return is_pa[0][n-1]

    #首先，DP，因为ispa[0,9]依靠ispa[0,8]和ispa[1,9](取最大值),所以如果n的range是从高到低。







if __name__ == "__main__":
    s = "asdasdajjdkajwiejladjkahsdjhawiueauwhdjashdjancnkjsahduiawudhajsnhsjahjdhawuahdjshjnzanjcnhjdashuawhdjaksndjkahduwhwauhdai"
    print(Solution.longestPalindromeSubseq(s))









