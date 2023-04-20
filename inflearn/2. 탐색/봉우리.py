import sys
# from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    board.insert(0, [0] * n)
    board.append([0] * n)
    for row in board:
        row.insert(0, 0)
        row.append(0)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = 0

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            is_mountain = True

            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]

                if board[x][y] <= board[next_x][next_y]:
                    is_mountain = False
                    break

            if is_mountain:
                res += 1

    print(res)
