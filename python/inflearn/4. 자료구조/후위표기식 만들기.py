import sys

if __name__ == "__main__":
    n = sys.stdin.readline()

    stack = []
    answer = ''
    for v in n:
        if v.isdecimal():
            answer += v
        elif v == "(":
            stack.append(v)
        elif v == "*" or v == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(v)
        elif v == "+" or v == "-":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(v)
        elif v == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()

    while stack:
        answer += stack.pop()

    print(answer)

