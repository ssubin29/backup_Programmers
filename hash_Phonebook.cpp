/*
해시-전화번호 목록
<어떻게 풀었는가?>
 전화번호의 값을 int가 아닌 string으로 준 이유가 있다. 
 sort할 경우 앞 부분이 같으면 나란히 정렬되기 때문이다. 
 따라서 정렬을 할 경우 하나하나 확인할 필요가 없어짐 앞부분이 비슷하다면 바로 옆에 나열되어있을 것이기 때문에. 
 루프를 총 2개 돌려 확인한다. 
 하나는 phone_book의 크기(전화번호의 개수)보다 하나 적게(하나 적은 이유는 마지막 전화번호는 확인할 필요 없기 때문), 
 그  안의 루프는 phone_book의 해당 인덱스에 위치하는 전화번호의 길이만큼 돌린다. 
 루프마다 i 인덱스와 i+1 인덱스에 위치한 값이 일치하는지 확인하고 하나라도 일치하지 않는 것이있다면 break하여 다음 전화번호로 간다. 
 만약 값이 전부 일치하는 경우를 찾았다면 바로 false를 return한다.
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());
    for (int i = 0; i < phone_book.size() - 1; i++)
    {
        for (int j = 0; j < phone_book[i].size(); j++)
        {
            if (phone_book[i][j] != phone_book[i + 1][j])
            {
                break;
            }
        }
        if (j == phone_book[i].size()) { return false; }
    }
    return answer;
}