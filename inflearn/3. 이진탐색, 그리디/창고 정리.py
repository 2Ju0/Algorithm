import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    l = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    arr.sort()
    for _ in range(m):
        arr[0] += 1
        arr[l-1] -= 1
        arr.sort()

    print(arr[l-1] - arr[0])
