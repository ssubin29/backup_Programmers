/*
해시-완주하지 못한 선수
*/

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> strMap;
    //map은 두 개의 인자를 가지는데, 첫 인자는 Key, 두 번째 인자는 Value 의 역할
    for (auto elem : completion) //auto 키워드를 사용하여 컴파일러가 자료형을 추론하도록
    {
        if (strMap.end() == strMap.find(elem))
            //end()는 빈 iterator의 주소 반환 find(a)의 경우 a를 찾지 못했으면 빈 iterator 주소 반환
            //그러므로 end()와 find(a)의 값이 같을 경우 = a의 값을 찾지 못했을 경우
            strMap.insert(make_pair(elem, 1));
        //insert(make_pair(key,value)) : pair 형태로 추가 (반드시)!!
        else
            strMap[elem]++;
    }

    for (auto elem : participant)
    {
        if (strMap.end() == strMap.find(elem)) { return elem; }
        else
        {
            strMap[elem]--;
            if (strMap[elem] < 0) { return elem; }
        }
    }
    return answer;
}