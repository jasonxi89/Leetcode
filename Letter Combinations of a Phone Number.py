NUMBERS={
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        results =[]
        self.dfs(digits, 0, "", results)
        return results


    def dfs(self, digits, index, path, results):
        if index == len(digits):
            results.append(path)
            return
        else:
            for letter in NUMBERS[digits[index]]:
                self.dfs(digits, index + 1, path + letter, results)
