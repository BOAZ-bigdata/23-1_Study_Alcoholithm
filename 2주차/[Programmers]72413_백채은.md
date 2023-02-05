# [Programmers 72413] 합승 택시 요금

## 문제
![image](https://user-images.githubusercontent.com/88718806/216805885-50023cc3-8887-4391-a29f-22a2c5ed3d96.png)

## 풀이
- 아이디어
  - 어디까지 합승할지. 그 지점을 찾기 => code에서 `k`
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
                    
                    
INF = 20000001
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
