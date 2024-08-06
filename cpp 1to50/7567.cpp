#include <iostream>
using namespace std;

int main() {
    string s, up, down;
    int h=10;
    cin >> s;
    
    for(int i=1;i<s.size();++i) {
        if(s[i]==s[i-1]) {
            h += 5;
        }
        else {
            h += 10;
        }
    }
    cout << h;
    system("pause");
    return 0;
}