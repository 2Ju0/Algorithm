def make_balanced_str(p):
    left = 0
    right = 0
    u = ""
    v = ""

    for i in range(len(p)):
        s = p[i]
        u += s
        if s == "(":
            left += 1
        else:
            right += 1
        if left == right:
            v = p[i+1:]
            break
    return u, v


def is_correct_str(p):
    stack = []
    for s in p:
        if s == "(":
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False

    return True


def reverse_str(p):
    answer = ""
    for s in p:
        if s == "(":
            answer += ")"
        else:
            answer += "("
    return answer


def solution(p):
    if p == "":
        answer = ""
    else:
        u, v = make_balanced_str(p)
        if is_correct_str(u):
            u += solution(v)
            answer = u
        else:
            answer = "(" + solution(v) + ")" + reverse_str(u[1:len(u)-1])

    return answer

