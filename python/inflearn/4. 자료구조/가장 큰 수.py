import sys

# 각 숫자 입장에서 앞에 오는 숫자는 본인보다 크면 안됨
if __name__ == "__main__":
    input = sys.stdin.readline
    nums, m = input().split()
    m = int(m)

    stack = []
    for num in nums:
        while stack and m > 0 and stack[-1] < num:
            if stack[-1] < num:
                stack.pop()
                m -= 1

        stack.append(num)

    if m != 0:
        stack = stack[:-m]

    print(''.join(stack))
