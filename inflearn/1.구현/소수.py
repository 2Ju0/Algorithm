import sys
import math

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    array = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    res = [num for num in array if num == True]
    print(len(res) - 2)

