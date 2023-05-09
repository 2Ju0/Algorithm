import sys


if __name__ == "__main__":
    n = sys.stdin.readline()

    stack = []
    for v in n:
        if v.isdecimal():
            stack.append(int(v))
        if v == "+":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2)
        elif v == "-":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 - op2)
        elif v == "*":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 * op2)
        elif v == "/":
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 / op2)

    print(stack[0])
