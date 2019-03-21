class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        result = []
        self.helper(n, []], result)
        return result


    def helper(self, n, path, result):
        if n == 0 :
            result.append(path[:])
            return
        path.append('(')
        path.append(')')
        self.helper(self, n-1, path, result)
        path.pop()
        self.helper(self, n-1, path, result)
        path.append(')')
