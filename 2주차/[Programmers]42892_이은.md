# [Programmers 42892.길 찾기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/42892?language=python3)
## 👾 풀이
  ### **`이진 탐색 트리, 트리 순회`**
- 문제 자체에서 이진 트리, 전위 순회, 후위 순회를 언급하기 때문에 트리 문제임은 쉽게 알 수 있었습니다.
- [x, y] 좌표값에 따라 이진 탐색 트리를 구현하였습니다.
- 29개의 테스트 케이스 중 2개의 테스트 케이스에서 런타임 에러가 발생했는데, 파이썬 재귀 limit이 1000이기 때문에 아래 코드를 맨 윗줄에 추가해서 해결했습니다. [관련 링크](https://school.programmers.co.kr/questions/3723?question=3723)
    ~~~python 
    import sys
    sys.setrecursionlimit(10**6)
    ~~~

## 👾 코드
~~~python
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.left = None
        self.right = None
        self.x = x
        self.y = y

class BinarySearchTree:
    def __init__(self, root):
        self.root = root
    
    def insert(self, next_node):
        self.current_node = self.root
        while True:
            if next_node.x < self.current_node.x:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(next_node.value, next_node.x, next_node.y)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(next_node.value, next_node.x, next_node.y)
                    break
    
    def preorder(self):
        arr = []
        def _preorder(node):
            arr.append(node.value)
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
        return arr
    
    def postorder(self):
        arr = []
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            arr.append(node.value)
        _postorder(self.root)
        return arr
                    
def solution(nodeinfo):
    sorted_nodeinfo = sorted(nodeinfo, key=lambda x:(-x[1], x[0]))
    root_node = sorted_nodeinfo[0]
    root = Node(nodeinfo.index(root_node) + 1, root_node[0], root_node[1])
    bst = BinarySearchTree(root)
    
    for node in sorted_nodeinfo[1:]:
        bst.insert(Node(nodeinfo.index(node) + 1, node[0], node[1]))
    
    return [bst.preorder(), bst.postorder()]
~~~