# [Programmers 17683: 방금 그곡](https://school.programmers.co.kr/learn/courses/30/lessons/17683)

전처리 제대로 할 수 있니...?

---

# 최종 코드

~~~python

# 시간 분단위로 변환 메소드
def time2min(time):
    min = int(time[0:2])*60 + int(time[3:5])
    return min

# 샵 전처리를 위한 변환 메소드
def replace_sharp(sound):
    return sound.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

def solution(m, musicinfos):
    answer_list = []
    m = replace_sharp(m)

    # 시작~끝난 시각까지 음을 연장 또는 단축
    for i in range(len(musicinfos)):
        song = musicinfos[i].split(',')

        song[3] = replace_sharp(song[3])
        song_time = (time2min(song[1]) - time2min(song[0]))
        tmp = song_time//len(song[3])
        tmp_rest = song_time%len(song[3])
        tmp_sound = song[3] * tmp + song[3][0:tmp_rest]

        # 음 단축 처리
        if(song_time < len(song[3])):
            tmp_sound = song[3][0:song_time]

        # m이 음 연장또는 단축한 거에 있나 확인
        if(m in tmp_sound):
            answer_list.append([song_time, song[1], song[2]])

    answer = ""
    if(len(answer_list)==0):
        answer = "(None)"
    else:
        tmp_sorted = sorted(answer_list, key = lambda x: (-x[0], x[1]))
        answer = tmp_sorted[0][2]
    return answer
~~~