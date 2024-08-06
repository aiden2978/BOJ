#include <iostream>
#include <conio.h>
using namespace std;

int main() {
    int a, b;
    while(1) {
        cin >> a >> b;
        if(a==0 and b==0) {
            break;
        }
        else {
            if(a>b) {
                cout << "Yes" << endl;
            }
            else {
                cout << "No" << endl;
            }
        }
    }
    getch();
    return 0;
}