#include <iostream>
#include <string>
using namespace std;

int main() {
    int N, a, b;
    string str;
    a = 0;
    b = 0;
    cin >> N;
    cin >> str;

    for(int i=0; i<N; ++i) {
        if(str[i] == 'A') {
            a += 1;
        }
        if(str[i] == 'B') {
            b += 1;
        }
    }

    if(a>b) {
        cout << "A";
    }
    if(a<b) {
        cout << "B";
    }
    if(a==b) {
        cout << "Tie";
    }
    system("pause");
    return 0;
}