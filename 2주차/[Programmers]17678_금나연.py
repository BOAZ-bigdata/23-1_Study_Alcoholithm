def time_calculator(time, reverse=False):
    # time(int) to str
    if (reverse):
        h = time // 60
        m = time % 60
        return "%02d:%02d" % (h, m)
    # str to time(int)
    else:
        h, m = time.split(":")[0], time.split(":")[1]
        return int(h) * 60 + int(m)


def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    time_int_table = [time_calculator(t) for t in timetable]  # time to int
    split_standard = [time_calculator(
        "09:00") + t * i for i in range(n)]  # n-1 for real

    # { shuttle_time : people_time_list }
    shuttle_dic = {}
    for time in split_standard:
        shuttle_dic[time] = []

    for time in time_int_table:
        for shuttle_time in split_standard:
            if (time <= shuttle_time) and len(shuttle_dic[shuttle_time]) < m:
                shuttle_dic[shuttle_time].append(time)
                break
            else:
                continue

    last_shuttle = time_calculator("09:00")+t*(n-1)
    # available
    if len(shuttle_dic[last_shuttle]) < m:
        answer = time_calculator(last_shuttle, True)
    # unavailable
    else:
        answer = time_calculator(shuttle_dic[last_shuttle][-1]-1, True)

    return answer
