def solution(phone_book):
    answer = True
    phone_book.sort()
    # 문자열은 sort할 경우 앞 부분부터 하나씩 비교한다 
    # ->  앞부분이 비슷하다면 그 다음으로 나열되어있겠구나!
    for i in range(len(phone_book)-1):
        for j in range(len(phone_book[i])):
            if (phone_book[i][j] != phone_book[i + 1][j]) :
                break;
        if (j == len(phone_book[i])-1) : 
            return False
    return answer