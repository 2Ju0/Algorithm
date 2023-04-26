def solution(id_list, report, k):
    report = list(set(report))  # 중복 신고 제거
    answer = {user: 0 for user in id_list}  # 메일 받은 횟수
    reporting_dic = {user: set() for user in id_list}  # 신고자 dict (누가 누구를 신고했는지)
    reported_dic = {user: 0 for user in id_list}  # 신고 횟수 dict (누가 몇번 신고 당했는지)

    for item in report:
        user, reported_user = item.split()
        reported_dic[reported_user] += 1
        reporting_dic.get(user).add(reported_user)

    for reported_user, cnt in reported_dic.items():
        if cnt >= k:
            for user, reported_users in reporting_dic.items():
                if reported_user in reported_users:
                    answer[user] += 1

    answer = list(answer.values())
    return answer
