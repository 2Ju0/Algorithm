import sys


def dfs(idx, cnt, sum):
    global answer

    if cnt == k:
        if sum % m == 0:
            answer += 1
            return
    else:
        for i in range(idx, n):
            dfs(i + 1, cnt + 1, sum + arr[i])


if __name__ == "__main__":
    input = sys.stdin.readline

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())

    answer = 0
    dfs(0, 0, 0)

    print(answer)
