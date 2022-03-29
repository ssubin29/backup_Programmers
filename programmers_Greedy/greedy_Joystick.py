# 탐욕법 - 조이스틱

import itertools

# 최단 경로를 찾아주는 함수
# 입력값 : 시작 인덱스, 목표 인덱스, 총 길이
def get_better_way(start, des, limit_len): 
    better = 0
    a = abs(des-start) # A~Z 사이를 왔다갔다 ex)'A'>'C'는 이게 좋음
    b = start + (limit_len - des) # Z를 넘아 A부터 ex) 'Z'>'C'는 이게 좋음
    return a if a < b else b

def solution(name):
    answer = 0
    theN = 65 # 시작은 A
    # A는 65 Z는 90
    
    # 인덱싱 리스트 만들기 Why? 이제부터 알파벳 완성 순서를 뒤바꿀거라 위치를 기억해두어야 함
    # 예를 들어, ZAF를 AFZ 순서로 완성하기 위해선 그 문자가 위치하는 인덱스를 알아내 
    # 그만큼 이동하는 조작까지 추가해야한다.
    indexing_list = {}
    for i in range(len(name)):
        if not name[i] in indexing_list.keys():
            indexing_list[name[i]] = [i]
        else:
            indexing_list[name[i]].append(i)
    print(indexing_list)
    
    # 이제부터 그리디 알고리즘의 진면목.. 조합을 사용하여 문자 완성 순서 뒤바꾸기
    orders = list(set((list(map(''.join, itertools.permutations(name))))))
    print(orders)
    
    # 그리고 각 문자 완성 순서대로 돌면서 최솟값 찾기
    # 중요한 것은 여기서 세는 것은 오직 조이스틱을 위아래로 조작한 횟수 뿐이다.
    alpha_len = ord('Z')-ord('A')
    print(alpha_len)
    answer_list = []
    for order in orders:
        count = 0
        start = get_better_way(0, ord(order[0])-ord('A'), alpha_len)
        # start는 첫번째 조작을 시작할 위치
        for alpha in order[1:]:            
            count = count + get_better_way(start, ord(alpha)-ord('A'), alpha_len)
        answer_list.append(count)
    print(answer_list)

    # 지금부터 세는 건 조이스틱을 왼쪽 오른쪽으로 이동시키는 횟수
    for i in range(len(orders)):
        order_list = []
        for alpha in orders[i]:
            order_list.append(indexing_list[alpha])
            #indexing_list.remove(indexing_list[alpha])
        count = 0
        start = get_better_way(0, order_list[0], len(name))
        for order in order_list[1:]:
            count = count + get_better_way(0, order, len(name))
    return answer

print(solution('ZAZ'))