# C. Bakry and Partitioning
class Node: # 바이너리 트리를 구성 할 노드 클래스 생성
    def __init__(self, data):
        self.data = data
        self.offspring = []

for step in range(int(input())):
    n, k = map(int,input().split())
    a_nums = list(map(int,input().split()))
    tree = []
    graph = {}
    for _ in range(n-1):
        f, t = map(int,input().split())
        graph[f] = t
        graph[t] = f
    for i in graph.keys():
        node = Node(i)
        node.offspring = graph[i]
