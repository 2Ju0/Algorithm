import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = list(input().rstrip())
    stack = []
    answer = 0

    while n:
        v = n.pop(0)
        if v == '(':
            if n[0] == ')':
                n.pop(0)
                l = len(stack)
                for _ in range(l):
                    stack.append(stack.pop(0) + 1)
            else:
                stack.append(1)
        else:
            answer += stack.pop()

    print(answer)
