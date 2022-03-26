# 탐욕법 - 조이스틱

import itertools

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
    print(list(map(''.join, itertools.permutations(name))))
    orders = (list(map(''.join, itertools.permutations(name))))
    
    # 그리고 각 문자 완성 순서대로 돌면서 최솟값 찾기
    # 중요한 것은 여기서 세는 것은 오직 조이스틱을 위아래로 조작한 횟수 뿐이다.
    answer_list = []
    for order in orders:
        count = 0
        for alpha in order:
            up = abs(ord('Z')-ord(alpha))  
            # A~Z 사이를 왔다갔다 ex)'A'>'C'는 이게 좋음
            down = (ord('Z')-ord(alpha))+(ord(alpha)-ord('A'))
            # Z를 넘아 A부터 ex) 'Z'>'C'는 이게 좋음
            count = count + up if up < down else count + down
        answer_list.append(count)
    
    # 지금부터 세는 건 조이스틱을 왼쪽 오른쪽으로 이동시키는 횟수
    for i in range(len(orders)):
        order_list = []
        for alpha in orders[i]:
            order_list.append(indexing_list[alpha])
            #indexing_list.remove(indexing_list[alpha])
        count = 0
        for order in order_list:
            in_count = (len(orders)-1) - order
            out_count = (len(orders)-1) - order
            #시발못해먹겠다
    return answer

print(solution('ZAZ'))

def get_better_way(start, des, limit_len): 
    better = 0
    return 