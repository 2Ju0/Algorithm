import math

if __name__ == "__main__":
    n = int(input().strip())

    for i in range(1, n + 1):
        v = int(input().strip())
        answer = float('inf')

        for j in range(1, int(math.sqrt(v)) + 1):
            if v % j == 0:
                cnt = (j - 1) + (v // j - 1)
                if cnt < answer:
                    answer = cnt

        print('#%d %d' % (i, answer))
