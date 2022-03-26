# 탐욕법 - 조이스틱

import itertools

# 최단 경로를 찾아주는 함수
# 입력값 : 시작 인덱스, 목표 인덱스, 총 길이
def get_better_way(start, des, limit_len): 
    better = 0
    a = abs(des-start) # A~Z 사이를 왔다갔다 ex)'A'>'C'는 이게 좋음
    b = start + (limit_len - des) + 1 # Z를 넘아 A부터 ex) 'Z'>'C'는 이게 좋음
    return a if a < b else b # 작은 거리 반환

def solution(name):
    answer = 0
    # A는 65 Z는 90
    
    # 알파벳과 알파벳이 위치해있는 인덱스 매핑
    indexing_list = {}
    for i in range(len(name)):
        if not name[i] in indexing_list.keys():
            indexing_list[name[i]] = [i]
        else:
            indexing_list[name[i]].append(i)
    print(indexing_list)

    # 중요한 것은 여기서 세는 것은 오직 조이스틱을 위아래로 조작한 횟수 뿐이다.
    alpha_len = ord('Z')-ord('A')
    updown_count = 0
    for alpha in name:
        updown_count = updown_count + get_better_way(0, ord(alpha)-ord('A'), alpha_len)    
    answer = answer + updown_count    

    # 이제부터 그리디 알고리즘의 진면목.. 조합을 사용하여 문자 완성 순서 뒤바꾸기
    orders = list(set((list(map(''.join, itertools.permutations(name))))))
    print(orders)

    return answer


print(solution("JAZ"))