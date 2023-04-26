def solution(s):
    answer = True
    stack = []

    for str in s:
        if str == "(":
            stack.append(str)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                return answer

    if stack:
        answer = False
    return answer
