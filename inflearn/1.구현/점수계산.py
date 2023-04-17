import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    res = [0 for _ in range(n)]
    is_cont = True

    for i in range(n):
        num = arr[i]

        if num == 1:
            if i > 0 and is_cont:
                res[i] = res[i-1] + 1
            else:
                res[i] = 1
            is_cont = True
        else:
            is_cont = False

    print(sum(res))
