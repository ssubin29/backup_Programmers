# 그래프 - 가장 먼 노드

from collections import deque
def solution(n, edge):
    answer = 0
    route = [0]*(n+1) #노드 1부터 각 노드까지의 거리
    edge.sort()    
    queue = deque() 
    graph = [[] for i in range(n+1)]
    
    for e in edge: # n번 노드와 연결되어있는 노드가 graph[n]에 저장되어있음
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    queue.append(1)
    route[1] = 1
    
    while queue:
        now = queue.popleft()
        for g in graph[now]:
            if route[g]==0:
                queue.append(g)
                route[g] = route[now]+1
    #print(graph)
    #print(route)
    
    # 1번 노드로부터 가장 멀리 떨어진 노드 개수 계산
    max_edge= max(route)
    for r in route:
        if r == max_edge:
            answer+=1     
    
    return answer