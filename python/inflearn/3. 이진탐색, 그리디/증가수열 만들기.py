import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    answer = ''
    prev = 0
    while arr:
        left = arr[0]
        right = arr[-1]
        tmp = []

        if left > prev:
            tmp.append((left, 'L'))
        if right > prev:
            tmp.append((right, 'R'))

        tmp.sort(key=lambda x: x[0])

        if not tmp:
            break

        prev = tmp[0][0]
        answer += tmp[0][1]

        if tmp[0][1] == 'L':
            arr.pop(0)
        else:
            arr.pop()

    print(len(answer))
    print(answer)
