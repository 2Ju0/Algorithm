import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    answer = [0] * n

    for i in range(n):
        for j in range(n):
            idx = arr[i]
            if arr[i] == 0 and answer[j] == 0:
                answer[j] = i + 1
                break
            elif answer[j] == 0:
                arr[i] -= 1

    for v in answer:
        print(v, end=' ')
