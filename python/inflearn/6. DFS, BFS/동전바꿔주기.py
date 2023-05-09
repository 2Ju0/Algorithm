import sys


def dfs(cnt, sum):
    global answer

    if sum > t:
        return
    if cnt == k:
        if sum == t:
            answer += 1
    else:
        for v in range(arr[cnt][1] + 1):
            dfs(cnt + 1, sum + arr[cnt][0] * v)


if __name__ == "__main__":
    input = sys.stdin.readline

    t = int(input())
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(k)]
    answer = 0

    dfs(0, 0)
    print(answer)
