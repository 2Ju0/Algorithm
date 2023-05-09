import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], x[0]))

    answer = 1
    prev = arr[0][1]
    for (start, end) in arr[1:]:
        if prev <= start:
            answer += 1
            prev = end

    print(answer)
