class Solution:
    """
    @param board: the given board
    @return: True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game
    """
    def validTicTacToe(self, board):
        # Write your code
        ["O  ", "   ", "   "]
        row = [board[i][0] + board[i][1]+board[i][2] for i in range(3)]
        column = [board[0][i] + board[1][i]+board[2][i] for i in range(3)]
        left_right = board[0][0]+board[1][1]+board[2][2]
        right_left = board[0][2]+board[1][1]+board[2][0]

        Xnums = board[0].count("X")+board[1].count("X")+board[2].count("X")
        Onums = board[0].count("O")+board[1].count("O")+board[2].count("O")

        Xwin = "XXX" in row or "XXX" in column or "XXX" == left_right or "XXX" ==right_left

        Owin = "OOO" in row or "OOO" in column or "OOO" == left_right or "OOO" ==right_left

        if Xnums == Onums:
            if not Xwin:
                return True
        elif Xnums == Onums +1:
            if not Owin:
                return True
        return False
