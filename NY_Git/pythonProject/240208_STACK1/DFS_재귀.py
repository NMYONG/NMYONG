'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(i): # 시작 i, 마지막 V
    visited[i] = 1       # 방문 표시
    print(i)             # 출력
    for w in adjl[i]:    # i에 인접하고 방문하지 않은 w가 있으면
        if visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접 리스트
adjl = [[] for _ in range(V+1)] # adjl[i] 행에 i에 인접한 정점번호
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 방향이 없는 경우

visited = [0] * (V+1)

dfs(1)