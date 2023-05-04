import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    answer = 0
    while arr:
        if len(arr) == 1:
            answer += 1
            break
        if arr[0] + arr[-1] <= m:
            arr.pop(0)
            arr.pop()
        else:
            arr.pop()

        answer += 1

    print(answer)
