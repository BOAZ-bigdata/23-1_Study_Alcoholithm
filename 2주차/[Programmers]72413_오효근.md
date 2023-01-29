# [Programmers 72413: 합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413)

처음 문제를 읽고 특정 지점에서 특정 지점까지의 최소 가중치를 구해야한다고 생각했다.

~~다익스트라 (Dijkstra) 알고리즘을 생각하고 풀었지만 사실 그것은 플로이드-워셜 (Floyd-Warshall) 알고리즘이였다.~~

최소 가중치를 출력하는 변수 `l`을 산출하였지만, 가장 큰 문제는 합승 유무 혹은 지점이였다.

따라서 브루트 포스 (Brute-force) 알고리즘을 통해 특정 지점까지 합승을 하였을 때의 최솟값으로 갱신해준 뒤 최종적으로는 합승을 하지 않았을 때의 값을 갱신해주어 `answer`를 리턴해주었다.

---

# 최종 코드

~~~python
import sys

def solution(n, s, a, b, fares):
    answer = sys.maxsize
    s -= 1
    a -= 1
    b -= 1
    l = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    for p1, p2, f in fares:
        l[p1 - 1][p2 - 1] = f
        l[p2 - 1][p1 - 1] = f
    for k in range(n):
        for i in range(n):
            for j in range(n):
                l[i][j] = min(l[i][j], l[i][k] + l[k][j])
    for i in range(n):
        if i == a:
            answer = min(answer, l[s][a] + l[a][b])
        elif i == b:
            answer = min(answer, l[s][b] + l[b][a])
        else:
            answer = min(answer, l[s][i] + l[i][a] + l[i][b])
    answer = min(answer, l[s][a] + l[s][b])
    return answer
~~~