/*
해시-위장
<어떻게 풀었는가?>
 바로 전 완주하지 못한 선수 문제를 활용하여 서로 다른 의상의 이름을 key로 개수를 value로 가지는 clothMap이라는 unordered_map 변수를 형성한다. 
 의상의 종류가 다를 경우 이름이 같더라도 하나만 입을 수 있거나 아예 입을 수 없다. 
 즉, 한 의상의 종류당 '종류는 같지만 이름은 다른 개수+1'가지의 선택을 할 수 있는 것이다. 
 이 선택을 매 의상마다 한다고 치면, (a+1)*(b+1)*(c+1)... 이런 식이 된다. 
 이렇게 계산한 뒤 아무것도 입지 않는 경우를 빼주면 우리가 찾는 값이다
*/
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {

    int answer = 1;
    unordered_map<string, int> clothMap;

    for (int i = 0; i < clothes.size(); i++)
    {
        string clo = clothes[i][1];
        if (clothMap.end() == clothMap.find(clo))
            clothMap.insert(make_pair(clo, 1));
        else
        {
            clothMap[clo]++;
        }
    }

    unordered_map<string, int>::iterator it;
    for (it = clothMap.begin(); it != clothMap.end(); it++)
    {
        answer *= (it->second) + 1;
    }
    return answer - 1;
}