import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    sum_list = []

    diagnal_neg = [board[i][i] for i in range(n)]
    diagnal_pos = [board[i][n-i-1] for i in range(n)]
    sum_list.append(sum(diagnal_neg))
    sum_list.append(sum(diagnal_pos))

    for i in range(n):
        column = [board[j][i] for j in range(n)]
        row = board[i]

        sum_list.append(sum(column))
        sum_list.append(sum(row))

    print(max(sum_list))


