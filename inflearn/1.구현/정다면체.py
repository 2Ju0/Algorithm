import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    count = dict()

    for first in range(1, n + 1):
        for second in range(1, m + 1):
            if first + second in count:
                count[first + second] += 1
            else:
                count[first + second] = 1

    max_num = max(count.values())
    res = [str(key) for (key, value) in count.items() if value == max_num]
    print(" ".join(res))
