/*
�ؽ�-��ȭ��ȣ ���
<��� Ǯ���°�?>
 ��ȭ��ȣ�� ���� int�� �ƴ� string���� �� ������ �ִ�. 
 sort�� ��� �� �κ��� ������ ������ ���ĵǱ� �����̴�. 
 ���� ������ �� ��� �ϳ��ϳ� Ȯ���� �ʿ䰡 ������ �պκ��� ����ϴٸ� �ٷ� ���� �����Ǿ����� ���̱� ������. 
 ������ �� 2�� ���� Ȯ���Ѵ�. 
 �ϳ��� phone_book�� ũ��(��ȭ��ȣ�� ����)���� �ϳ� ����(�ϳ� ���� ������ ������ ��ȭ��ȣ�� Ȯ���� �ʿ� ���� ����), 
 ��  ���� ������ phone_book�� �ش� �ε����� ��ġ�ϴ� ��ȭ��ȣ�� ���̸�ŭ ������. 
 �������� i �ε����� i+1 �ε����� ��ġ�� ���� ��ġ�ϴ��� Ȯ���ϰ� �ϳ��� ��ġ���� �ʴ� �����ִٸ� break�Ͽ� ���� ��ȭ��ȣ�� ����. 
 ���� ���� ���� ��ġ�ϴ� ��츦 ã�Ҵٸ� �ٷ� false�� return�Ѵ�.
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