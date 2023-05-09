import sys


def dfs(v, cnt):
    global total

    if cnt == m:
        total += 1
        print(' '.join([str(i) for i in answer]))
        return
    if v > n:
        return
    else:
        answer[cnt] = v
        dfs(v + 1, cnt + 1)
        answer[cnt] = 0
        dfs(v + 1, cnt)


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    answer = [0] * m
    total = 0

    dfs(1, 0)
    print(total)
