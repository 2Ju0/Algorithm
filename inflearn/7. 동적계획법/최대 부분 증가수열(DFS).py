import sys


def dfs(cnt):
    global answer

    if cnt == n:
        tmp = []
        for i in range(n):
            if ch[i] == 1:
                tmp.append(arr[i])
        if len(tmp) != 0:
            prev = tmp[0]
            for v in tmp[1:]:
                if v <= prev:
                    break
                prev = v
            else:
                answer = max(answer, len(tmp))
    else:
        ch[cnt] = 1
        dfs(cnt + 1)
        ch[cnt] = 0
        dfs(cnt + 1)


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    ch = [0] * n

    answer = 0
    dfs(0)
    print(answer)
