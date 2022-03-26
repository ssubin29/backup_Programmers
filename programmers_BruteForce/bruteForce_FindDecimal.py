# 완전탐색 - 소수 찾기

import itertools
import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
    # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    decimal_list = []
    for i in range(1,len(numbers)+1):
        ll = list(set(map(int,map(''.join, itertools.permutations(numbers,i)))))
        print(ll)
        for l in ll:
            if is_prime_number(l):
                print(f'{l}은 소수이다')
                decimal_list.append(l)
    decimal_list = len(list(set(decimal_list)))
    
    return decimal_list