# [Programmers 72411: 메뉴 리뉴얼](https://school.programmers.co.kr/learn/courses/30/lessons/72411)

Brute force로 풀면,, 시간 초과가 나기때문에 hash 구조를 이용하여 푼다!

각 케이스에 따라서 출현 횟수를 기입!

---

# 최종 코드

~~~python
from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        ord = {}
        for order in orders:
            for tmporder in combinations(sorted(order), c):
                tmp = ''.join(tmporder)
                if tmp in ord:
                    ord[tmp] += 1
                else:
                    ord[tmp] = 1
        for tmporder in ord:
            if ord[tmporder] == max(ord.values()) and ord[tmporder] > 1:
                answer.append(tmporder)
    answer.sort()
    return answer
~~~