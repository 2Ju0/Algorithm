import sys


if __name__ == "__main__":
    input = sys.stdin.readline

    board = [list(map(int, input().split())) for _ in range(9)]
    is_right = True

    # 행, 열 검사
    for i in range(9):
        row = board[i]
        column = [board[j][i] for j in range(9)]

        if len(set(row)) != 9 or len(set(column)) != 9:
            is_right = False
            break

    # 3 x 3 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]

            if len(set(tmp)) != 9:
                is_right = False
                break

        if not is_right:
            break

    print("YES" if is_right else "NO")
