#include <iostream>
#include <string>
#include <conio.h>
using namespace std;

int main() {
    string a, b, two;
    char sgn;
    two = '2';

    cin >> a;
    cin >> sgn;
    cin >> b;

    if(sgn == '*') {
        cout << a + b.substr(1);
    }
    if(sgn == '+') {
        if(a.size() == b.size()) {
            cout << a.replace(0, 1, two);
        }
        if(a.size() > b.size()) {
            cout << a.replace(a.size() - b.size(), b.size(), b);
        }
        if(a.size() < b.size()) {
            cout << b.replace(b.size() - a.size(), a.size(), a);
        }
    }

    getch();
    return 0;
}