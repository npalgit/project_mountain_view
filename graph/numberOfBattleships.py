#!/usr/bin/python
"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them
"""
def countBattleship(board):
    count = 0
    w, h = len(board[0]), len(board)
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'X':
                count += 1
                markBoard(board, i, j)

    return count

def markBoard(board, i, j):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return

    if board[i][j] == 'X':
        board[i][j] = '.'
        markBoard(board, i+1, j)
        markBoard(board, i-1, j)
        markBoard(board, i, j+1)
        markBoard(board, i, j-1)

def test1():
    board = ['X..X', '...X', '...X']
    board = map(list, board)
    print(countBattleship(board))

def test2():
    board = ['...X', 'XX..','...X']
    board = map(list, board)
    print(countBattleship(board))

if __name__ == '__main__':
    test1()
    test2()
