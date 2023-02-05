# [Programmers 17678] [1차] 셔틀버스

## 문제
- 셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
- 셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다.  
  예를 들어 09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루도 탈 수 있다.

## 풀이
- floyd-warshall 알고리즘

## code

~~~python
### floyd-warshall 알고리즘
def floyd(dist, n):
    for k in range(n): # k : 거쳐가는 노드
        for i in range(n): # i : 출발 노드
            for j in range(n): # j : 도착 노드
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j] # dist[] : 모든 출발점과 도착점의 최소비용
                    
                    
INF = 40000000
def solution(n, s, a, b, fares):
    answer = 0
    
    lst = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        lst[i][i] = 0
        
    for i, j, f in fares:
        lst[i][j] = f
        lst[j][i] = f
        
    floyd(lst, n+1)
    
    answer = INF
    for k in range(n+1):
        answer = min(answer, lst[s][k] + lst[k][a] + lst[k][b])
    
    return answer
~~~
