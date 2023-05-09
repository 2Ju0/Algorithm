import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = list(input().rstrip())
    stack = []
    answer = 0

    for i in range(len(n)):
        if n[i] == '(':
            stack.append(n[i])
        else:
            stack.pop()
            if n[i - 1] == '(':
                answer += len(stack)
            else:
                answer += 1
    print(answer)
