# [Programmers 17678] [1차] 셔틀버스

## 문제
- 셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
- 셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다.  
  예를 들어 09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루도 탈 수 있다.

## 풀이
- 아이디어
  - `시:분`을 `str`에서 `int`로 바꾸기 (분 단위로 통일)
- 풀이 순서
  1. `crews[]`에 크루의 도착시간 저장
  2. `crews[]` 정렬 (먼저 온 크루가 앞으로)
  3. `buses[]`에 09:00부터 n회 t분 간격으로 역에 도착하는 버스 시간 저장
  4. 버스가 도착할 때마다 버스에 타는 크루의 수(`cnt`) 구하기
  5. 버스에 자리가 남는 경우 콘은 버스 도착 시간에 도착
  6. 버스에 자리가 없을 경우 콘은 맨 마지막에 버스에 탄 크루보다 1분 먼저 도착

## code
### - 정답
~~~python
def solution(n, t, m, timetable):
    answer_int = 0
    answer = ''
    
    crews = []
    for i in timetable:
        i = i.split(':')
        bun = int(i[0])*60 + int(i[1])
        crews.append(bun)
        
    crews.sort()
    
    buses = []
    for i in range(n):
        bun = 9*60 + t*i
        buses.append(bun)

    ####################################################
    
    j = 0 # 다음에 버스에 탈 크루의 인덱스
    for i in range(len(buses)): # 버스가 도착 할 때마다
        cnt = 0 # 버스에 타는 크루 수
        
        while j < len(crews) and cnt < m and crews[j] <= buses[i]:
            j += 1
            cnt += 1
                
        if cnt < m: # 버스에 자리가 남는 경우
            answer_int = buses[i] # 버스 도착 시간
        else: # 버스에 자리가 없는 경우
            answer_int = crews[j-1]-1 # 맨 마지막에 버스에 탄 크루보다 1분 먼저

    ####################################################
   
    a, b = str(answer_int // 60), str(answer_int % 60)
    if len(a) == 1: a = '0' + a
    if len(b) == 1: b = '0' + b
    answer += a + ':' + b
    return answer
~~~
### - 시도한 오답
~~~python
    ####################################################
    cnts = []
    jj = 0 
    for i in range(len(buses)): # 버스가 도착 할 때마다
        cnt = 0 # 버스에 타는 크루 수
        
        for j in range(len(crews)):
            if crews[j] <= buses[i]:
                cnt += 1
                jj = j
            else:
                break
                
        cnts.append(cnt)
            
    for i in range(len(buses)):
        if cnts[i] < m: # 버스에 자리가 남는 경우
            answer_int = buses[i] # 버스 도착 시간
        else: # 버스에 자리가 없을 경우
            answer_int = crews[jj]-1 # 맨 마지막에 버스에 탄 크루보다 1분 먼저

    ####################################################
~~~
