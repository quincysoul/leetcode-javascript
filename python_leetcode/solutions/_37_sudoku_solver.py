from typing import List
import math
import time

"""
Summary:

Trick:
    A few options:
    1. Backtracking
    2. DFS
    - And, ds options of stack, deque, or system stack via recurse.
    The brute force is to try every possible number combination, O(9^N)
    This question is known to be asked in phone interviews.

Bibliography:
    Solution source: techwithtim:
    https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/

Args:
    board (List[List]): 2d array of a valid sudoku board, as below.
    example_board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
"""


class Solution:
    def __init__(self):
        self.len_board = 9
        self.n = 1
        self.n_expected = "Unknown O(N)"
        self.unsolved = []

    # Now we know if any given element is valid, we can look at all the elements
    # and try different values if not valid
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.unsolved = self.find_unsolved(board)
        print("Board to solve:\n----------------")
        self.pretty_print(board, 0, 0)
        # print(f"Unsolved elements: {self.unsolved}")
        # self.pretty_print_unsolved(board)

        i = 0
        while i < len(self.unsolved):
            position = self.unsolved[i]
            # print(f"Attempting to solve position: {position}")
            # self.pretty_print(board, *position)

            # Increment position element
            current_value = self.quick_get(board, *position)
            # Check if position element is valid.
            print(f"checking if positon is valid: {position}")
            if self.quick_get(board, *position) == 10:
                # Current position is invalid, set to 0 and backtrack.
                print(f"hit unsolveable at position: {position}")
                self.quick_set(board, *position, 0)
                i -= 1
                # Previous position answer only appeared valid until we hit this position.
                # Increment the previous position and try from there.
                backtrack_position = self.unsolved[i]
                backtrack_value = self.quick_get(board, *backtrack_position)
                self.quick_set(board, *backtrack_position, (backtrack_value + 1))
            elif self.is_valid(board, *position):
                # Position is valid, so move forward to the next unsolved item in the list.
                print("Found valid number,")
                self.pretty_print(board, *position)
                i += 1
                continue
            else:
                self.quick_set(board, *position, (current_value + 1))
                # Remain on position and re-check validity at incremented value.
            if position[0] == 8 and position[1] == 6:
                self.pretty_print(board, *position)
            # print(f"Position was not valid, remaining on position: {position}")

        # End while (iteration through unsolved elements)
        return board

    def is_valid(self, board, i, j):
        element = self.quick_get(board, i, j)

        # Validate row.
        for col in range(self.len_board):
            if col != j and element == self.quick_get(board, i, col):
                return False
        # Validate col.
        for row in range(self.len_board):
            if row != i and element == self.quick_get(board, row, j):
                return False
        # Validate 3x3 box.
        """
        Get the box coordinates like so.
        [0,0] [0,1] [0,2]
        [1,0] [1,1] [1,2]
        [2,0] [2,1] [2,2]
        """
        bI = i // 3
        bJ = j // 3
        # Take box coordinates, and then get the starting i,j index by multiplying each by 3.
        sI = bI * 3
        sJ = bJ * 3

        for h in range(3):
            for w in range(3):
                if (
                    sI + h != i
                    and sJ + w != j
                    and self.quick_get(board, sI + h, sJ + w) == element
                ):
                    return False
        # No invalid copies of this element were found, so is_valid res True.
        return True

    def quick_set(self, board, i, j, val):
        board[i][j] = str(val)

    def quick_get(self, board, i, j):
        return int(board[i][j])

    def find_unsolved(self, board):
        unsolved = []
        for i in range(self.len_board):
            for j in range(self.len_board):
                if board[i][j] == "." or board[i][j] == " " or board[i][j] == "":
                    board[i][j] = "0"
                    unsolved.append([i, j])
        return unsolved

    def print_n(self):
        print(f"O(N): {self.n}/{self.n_expected}")

    def pretty_print(self, board, i, j):
        for h in range(self.len_board):
            for w in range(self.len_board):
                if h == i and w == j:
                    print(f"[{board[i][j]}]", end="")
                else:
                    print(f" {board[h][w]} ", end="")
                if w == 8:
                    print("")

    def pretty_print_unsolved(self, board):
        for h in range(self.len_board):
            for w in range(self.len_board):
                if [h, w] in self.unsolved:
                    print(f"[{board[h][w]}]", end="")
                else:
                    print(f" {board[h][w]} ", end="")
                if w == 8:
                    print("")
