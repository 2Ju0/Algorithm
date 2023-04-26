import sys
import math


def getDigit(x):
    res = ""

    for s in x:
        if s.isdigit():
            res += s

    res = int(res.lstrip("0"))
    return res


def getDivisor(x):
    res = 0

    for i in range(1, int(math.sqrt(x) + 1)):
        if x % i == 0:
            res += 1
            if i != (x // i):
                res += 1
    return res


if __name__ == "__main__":
    input = sys.stdin.readline
    num = getDigit(input())

    print(num)
    print(getDivisor(num))
