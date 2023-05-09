import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (-x[1], -x[0]))

    answer = 1
    max_h = arr[0][0]
    for (h, w) in arr[1:]:
        if h > max_h:
            max_h = h
            answer += 1

    print(answer)
