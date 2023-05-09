import sys


def dfs(v, cnt):
    global total

    if cnt == m:
        total += 1
        print(' '.join(str(i) for i in answer))
    else:
        for i in range(v, n + 1):
            answer[cnt] = i
            dfs(i + 1, cnt + 1)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())

    answer = [0] * m
    total = 0

    dfs(1, 0)
    print(total)
