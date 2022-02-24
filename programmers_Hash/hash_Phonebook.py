# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     # 문자열은 sort할 경우 앞 부분부터 하나씩 비교한다 
#     # ->  앞부분이 비슷하다면 그 다음으로 나열되어있겠구나!
#     for i in range(len(phone_book)-1):
#         for j in range(len(phone_book[i])):
#             if (phone_book[i][j] != phone_book[i + 1][j]) :
#                 break;
#         if (j == len(phone_book[i])-1) : 
#             return False
#     return answer

# 위는 	["119", "114", "112", "123223123", "1231231234"]를 만족하지 못함
# 왜? 112 114 상황일 때 2,4가 달라 루프 밖으로 나오면
# if (j == len(phone_book[i])-1) : return False 에서 False가 되기 때문이다
# c++에서는 for(j=0; j<phone_book[i].size(); j++)여서 
# 루프문을 다 돈다면 j가 len(phone_book[i])와 같아지기 때문에 괜찮았지만
# 파이썬에서는 range를 사용했으므로 루프문을 다돈다면 j는 len(phone_book[i])보다 1 작은 값을 갖게 된다
# 그래서 C++에서는 잘 돌아갔지만 파이썬에선 몇 사례에서 오류가 뜬 것

def solution(phone_book):
    answer = True
    phone_book.sort()
    # 문자열은 sort할 경우 앞 부분부터 하나씩 비교한다 
    # ->  앞부분이 비슷하다면 그 다음으로 나열되어있겠구나!
    for i in range(len(phone_book)-1):
        for j in range(len(phone_book[i])):
            if (phone_book[i][j] != phone_book[i + 1][j]) :
                break;
        if ((j == len(phone_book[i])-1) 
            and (phone_book[i][j] == phone_book[i+1][j])): 
            return False
    return answer