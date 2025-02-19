def bfs(start):
    Q = []  # 빈 스택 생성
    visited = [False] * (N + 1)  # 방문하면 False -> True

    Q.append(start)  # start(시작번호)를 Q에 넣음
    visited[start] = True  # 시작번호의 노드를 다시 가지 않도록 visited에 저장

    while Q:  # Q가 비어있지 않다면 계속 실행
        v = Q.pop(0)  # Q의 첫번째 원소 꺼내기
        print(v)

        for w in G[v]:  # w = G[v]에서 갈 수 있는 Node
            if not visited[w]:  # False일 때 아래 실행 ==> if visited[w] == False / 방문하지 않았다면
                Q.append(w)
                visited[w] = True  # 재방문 하지 않기 위해서 True로 설정


s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
l = list(map(int, s.split()))

N = 7  # 노드의 개수 (Node)
E = len(l)  # 경로의 개수 * 2 (Edge)
G = [[] for _ in range(N + 1)]  # 리스트는 인덱스가 0부터 시작하므로 N+1 (Graph)
# G = [[], [], [], [], [], [], [], []]

for i in range(0, E, 2):  # i = 0, 2, 4, ... 경로가 1문장으로 주어졌기 때문에
    v1 = l[i]  # vertex (정점) / v1 = 1, 1, 2, 2, 4, 5, 6, 3
    v2 = l[i + 1]  # 2, 3, 4, 5, 6, 6, 7, 7

    G[v1].append(v2)  # 방향이 있을 경우
    G[v2].append(v1)  # 방향이 없는 경우(양방향)

print(G)
bfs(1)