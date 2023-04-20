import sys


def countPalindrome(arr):
    res = 0

    for i in range(3):
        tmp = arr[i:i + 5]
        reversed_tmp = tmp[::-1]

        if tmp == reversed_tmp:
            res += 1

    return res


if __name__ == "__main__":
    input = sys.stdin.readline

    board = [input().split() for _ in range(7)]
    res = 0

    for i in range(7):
        row = board[i]
        column = [board[j][i] for j in range(7)]

        res += countPalindrome(row)
        res += countPalindrome(column)

    print(res)
