import sys
from collections import deque


def rotate(board, index, direction, count):
    row = deque()
    row.extend(board[index - 1])

    for _ in range(count):
        if direction == 0:
            item = row.popleft()
            row.append(item)
        else:
            item = row.pop()
            row.appendleft(item)

    return list(row)


def sumArea(board):
    res = 0
    length = len(board)
    mid = length // 2

    for i in range(length):
        row = board[i]
        if i <= mid:
            res += sum(row[i:length - i])
        else:
            res += sum(row[length - i - 1:i + 1])

    return res


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    m = int(input())
    for _ in range(m):
        index, direction, count = map(int, input().split())
        row = rotate(board, index, direction, count)
        board[index-1] = row

    print(sumArea(board))
