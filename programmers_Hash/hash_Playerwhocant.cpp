/*
�ؽ�-�������� ���� ����
*/

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> strMap;
    //map�� �� ���� ���ڸ� �����µ�, ù ���ڴ� Key, �� ��° ���ڴ� Value �� ����
    for (auto elem : completion) //auto Ű���带 ����Ͽ� �����Ϸ��� �ڷ����� �߷��ϵ���
    {
        if (strMap.end() == strMap.find(elem))
            //end()�� �� iterator�� �ּ� ��ȯ 
            //find(a)�� ��� a�� ã�� �������� �� iterator �ּ� ��ȯ
            //�׷��Ƿ� end()�� find(a)�� ���� ���� ��� = a�� ���� ã�� ������ ���
            strMap.insert(make_pair(elem, 1));
        //insert(make_pair(key,value)) : pair ���·� �߰� (�ݵ��)!!
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