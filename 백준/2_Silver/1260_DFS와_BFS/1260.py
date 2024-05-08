from collections import deque


def bfs(i, visit, graph):
    """너비 우선 탐색"""
    queue = deque([i])
    visit[i] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        # 연결된 모든 노드 탐색
        for num in graph[v]:
            if not visit[num]:
                # num 노드를 방문하지 않았으면
                visit[num] = True
                queue.append(num) # 방문 하기 위해 queue에 추가


def dfs(i, visit, graph):
    """깊이 우선 탐색"""
    visit[i] = True
    print(i, end=" ") # i 노드 방문 후 print

    for num in graph[i]:
        if not visit[num]:
            # i 노드에 연결된 노드 중 방문하지 않은 노드가 있으면 방문
            dfs(num, visit, graph)


def main():
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 정렬(순차적으로 돌기 위함)
    for i in graph:
        i.sort()

    # dfs
    visit = [False] * (n+1)
    dfs(v, visit, graph)
    print()

    # bfs
    visit = [False] * (n+1)
    bfs(v, visit, graph)

main()