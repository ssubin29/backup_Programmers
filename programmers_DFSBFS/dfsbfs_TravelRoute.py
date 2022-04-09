# 깊이/너비 우선 탐색(DFS/BFS) - 여행경로

from collections import deque

# BFS 함수 정의
def bfs(dict_of_ticket, start, length):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[i] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def solution(tickets):
    answer = []
    dict_t = {} # tickets를 dict 형태로 변환
    
    for i in range(len(tickets)):
        if tickets[i][0] in dict_t.keys():
            dict_t[tickets[i][0]].append(tickets[i][1])
        else:
            dict_t[tickets[i][0]] = [tickets[i][1]]
    print(dict_t)
    
    length = len(dict_t.keys())    
    #visited = [False] * length
    dfs(dict_t, "ICN", length)
        
    
    return answer