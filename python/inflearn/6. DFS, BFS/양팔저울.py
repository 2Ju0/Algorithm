import sys


def dfs(cnt, sum):
    global answer

    if cnt == n:
        if 0 < sum <= s:
            answer.add(sum)
    else:
        dfs(cnt + 1, sum + arr[cnt])  # 추를 저울의 왼쪽에
        dfs(cnt + 1, sum - arr[cnt])  # 추를 저울의 오른쪽에
        dfs(cnt + 1, sum)  # 추를 사용하지 않음


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)
    answer = set()

    dfs(0, 0)
    print(s - len(answer))
