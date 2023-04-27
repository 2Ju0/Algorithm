def slice_word(s, i):
    lst = []
    cnt = 0
    tmp_str = ""

    for str in s:
        tmp_str += str
        cnt += 1
        if cnt == i:
            lst.append(tmp_str)
            cnt = 0
            tmp_str = ""
    if tmp_str != "":
        lst.append(tmp_str)

    return lst


def solution(s):
    answer_dict = {i: 0 for i in range(1, len(s)+1)}

    for i in range(1, len(s)+1):
        sliced_word_lst = slice_word(s, i)
        flag = ""
        result = ""
        cnt = 0

        for idx in range(len(sliced_word_lst)):
            word = sliced_word_lst[idx]

            if idx == 0:
                flag = word
                cnt += 1
                continue
            if flag != word:
                if cnt == 1:
                    result += flag
                else:
                    result += (str(cnt) + flag)
                flag = word
                cnt = 1
            else:
                cnt += 1

        if cnt == 1:
            result += flag
        else:
            result += (str(cnt) + flag)
        answer_dict[i] = len(result)

    answer = min(list(answer_dict.values()))
    return answer