import unittest
import logging
from typing import List

LOG = logging.getLogger(__name__)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we need to check following keys duplicate or not, for all the non "." value
        # rows: (row, value)
        # cols: (col, value)
        # block (row // 3, col // 3, value)
        row_set = set()
        col_set = set()
        block_set = set()
        for row_idx, row in enumerate(board):
            for col_idx, value in enumerate(row):
                if value == ".":
                    continue
                # row check
                row_key = (row_idx, value)
                if row_key in row_set:
                    return False
                else:
                    row_set.add(row_key)
                # col check
                col_key = (col_idx, value)
                if col_key in col_set:
                    return False
                else:
                    col_set.add(col_key)

                # block check
                block_key = (row_idx // 3, col_idx // 3, value)
                if block_key in block_set:
                    return False
                else:
                    block_set.add(block_key)

        return True

    def isValidSudoku_x(self, board: List[List[str]]) -> bool:
        # need to check rows and cols and every 3x3

        # rows:
        for row in board:
            valid_num = [i for i in row if i != "."]
            if len(valid_num) != len(set(valid_num)):
                return False

        # cols
        for col_idx in range(9):
            valid_num = [i[col_idx] for i in board if i[col_idx] != "."]
            if len(valid_num) != len(set(valid_num)):
                return False

        # every 3x3
        strip = 3
        for row_block in range(3):
            row_start = strip * row_block
            row_block_idx = range(row_start, row_start + 3)
            for col_block in range(3):
                col_start = strip * col_block
                col_block_idx = range(col_start, col_start + 3)

                valid_num = [
                    board[i][j] for i in row_block_idx for j in col_block_idx if board[i][j] != "."
                ]
                if len(valid_num) != len(set(valid_num)):
                    return False
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        obj = Solution()
        assert obj.isValidSudoku(board) == True

    def test2(self):
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        obj = Solution()
        assert obj.isValidSudoku(board) == False
