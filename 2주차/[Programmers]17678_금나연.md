# [Programmers 17678] [1차] 셔틀버스

## 문제 요약

1. 셔틀은 `09:00`부터 총 `n`회 `t`분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 `m`명의 승객이 탈 수 있다.

- 크루가 대기열에 도착하는 시각을 모은 배열 `timetable`

2. 셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다. 예를 들어 09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루도 탈 수 있다.

## 목표

셔틀을 타고 사무실로 갈 수 있는 <b>도착 시각 중 `제일 늦은` 시각</b>을 구하여라.

### 예제 입력

```
2, 10, 2, ["09:10", "09:09", "08:00"]
```

### 예제 출력

```
"09:09"
```

## 풀이

- `빡구현`

### 주요 논리

#### 1. 시간을 숫자로, 또는 숫자를 시간으로 변경하는 time_calculator

```python
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
```

- ex1) "09:01" -> 541
- ex2) 549 -> "09:09"

## 전체 코드

```python
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

```

## 개선점

- 굳이 dic이나 리스트로 저장하지 않아도 될 것 같음
