# [Programmers 17683](https://school.programmers.co.kr/learn/courses/30/lessons/17683) 방금그곡

## 문제 요약

1. 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B `12개`

2. 각 음은 1분에 1개씩 재생, 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생

## 목표

- 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 `재생된 시간이 제일 긴 음악 제목`을 반환, 재생된 시간도 같을 경우 `먼저 입력된 음악 제목`을 반환
- 조건이 일치하는 음악이 없을 때에는 `“(None)”`을 반환

### 예제 입력

```
m="CC#BCC#BCC#BCC#B"
musicinfos=["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
```

### 예제 출력

```
"FOO"
```

- BAR의 경우 반복이 8까지 끊기므로 조건 만족 x
- FOO의 경우 30분 동안 지속되므로 조건 만족 o

## 풀이

- `구현`

### 주요 논리

#### 1. 시간 -> 총 분

```python
def time_calculator(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)
```

#### 2. # 대체

```python
def map_syllables(m):
    return m.replace("C#", "1").replace("D#", "2").replace("F#", "3").replace("G#", "4").replace("A#", "5")
```

## 전체 코드

```python
def time_calculator(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)


def map_syllables(m):
    return m.replace("C#", "1").replace("D#", "2").replace("F#", "3").replace("G#", "4").replace("A#", "5")


def solution(m, musicinfos):
    answer = {"name": "", "whole_music": ""}
    for music in musicinfos:
        start, end, name, part = music.split(",")
        m, part = map_syllables(m), map_syllables(
            part)  # map both test and vaildation
        part *= 1439  # max
        whole_music = part[:time_calculator(
            end)-time_calculator(start)]  # duration
        if m in whole_music:
            if len(whole_music) > len(answer["whole_music"]):
                answer["name"], answer["whole_music"] = name, whole_music
    if (answer["name"]):
        return answer["name"]
    else:
        return "(None)"
```
