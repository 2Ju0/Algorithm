import sys


def dfs(cnt, s):
    global answer
    if cnt == len(n):
        answer += 1
        print(s)
    else:
        for i in range(1, 3):
            num = n[cnt:cnt+i]
            if num[0] == '0':
                continue
            if i == 2 and cnt == len(n) - 1:
                continue
            if int(num) <= 26:
                dfs(cnt + i, s + chr(int(num) + 64))


if __name__ == "__main__":
    n = sys.stdin.readline().strip()  # 아스키 A -> 65
    answer = 0

    dfs(0, '')
    print(answer)

