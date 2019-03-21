class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

#stack方法
    def expressionExpand(self, s):

        stack = []
        for c in s:
            if c != ']':
                stact.append(c)
            else:
                strs = []
                while stack and stack[-1] != '[]':
                    strs.append(stack.pop())

                stack.pop()

                repeats = 0
                base = 1
                while stack and stack[-1].isdigit():
                    repeats += (ord(stack.pop())-ord('0')) * base
                    base *= 10
                stack.append(''.join(reversed(strs))* repeats)
        return ''.join(stack)
#递归
    def expressionExpand(self, s):
         if not s:
             return None
        res, _ = self.helper(0,s)
        return res


    def helper(pos, s):
        res = ''
        num = 0
        while  pos < len(s):
            if s[pos].isalpha():
                res += s[pos]
            elif s[pos].isdigit():
                num = 10 * num + int(s[pos])
            elif s[pos] == '[':
                substring, pos =self.helper(pos+1, s)
                res += substring * num
                num = 0
            elif s[pos] ==']'
                return res, pos
            pos +=1
        return res,pos
