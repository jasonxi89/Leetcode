class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    # def calculate(self, s):
    #     # Write your code here
    #     if not s:
    #         return 0
    #     while s.rfind("(") != -1:
    #         left = s.rfind("(")
    #         right = s[left:].find(")")+ left
    #         num = self.helper(self,s[left+1:right])
    #         if right + 1 >= len(s):
    #             s = s[:left] + str(num)
    #         else:
    #             s = s[:left]+ str(num) + s[right+1:]
    #     return self.helper(self,s)
    #
    #
    #
    #
    # def helper(self,cut):
    #     num = 0
    #     for i in range(len(cut) - 1, 0, -1):
    #         if cut[i] == "+":
    #             num += int(cut[i + 1:])
    #             cut = cut[:i]
    #         elif cut[i] == "-":
    #             if i - 1 >= 0 and cut[i-1] == "-":
    #                 num += int(cut[i + 1:])
    #                 cut = cut[:i-1]
    #                 i -= 1
    #                 continue
    #             num -= int(cut[i + 1:])
    #             cut = cut[:i]
    #     num += int(cut)
    #     return num
    # 抄个高票答案
    # def calculate(selfs,s):
    #     res, num, sign, stack = 0, 0, 1, []
    #     for ss in s:
    #         if ss.isdigit():
    #             num = 10 * num + int(ss)
    #         elif ss in ["-", "+"]:
    #             res += sign * num
    #             num = 0
    #             sign = [-1, 1][ss == "+"]
    #         elif ss == "(":
    #             stack.append(res)
    #             stack.append(sign)
    #             sign, res = 1, 0
    #         elif ss == ")":
    #             res += sign * num
    #             res *= stack.pop()
    #             res += stack.pop()
    #             num = 0
    #     return res + num * sign
    #
    def calculate(selfs, s):
        #sign + = 1, - = -1
        res, num, sign, stack = 0,0,1,[]
        for ss in s:
            if ss.isdigit():
                num = 10* num + int(ss)
            elif ss in["-","+"]:
                #deal with last number
                res += num * sign
                num = 0
                sign = [-1 , 1] [ss == "+"]
            elif ss =="(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0,1
            elif ss ==")":
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res +  num * sign


__name__ == "__main__"
print(Solution.calculate(Solution,"1-(2+3-(4+(5-(1-(2+4-(5+6))))))"))