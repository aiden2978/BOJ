#include <iostream>
#include <conio.h>

using namespace std;

int main() {
    int a, sum;
    sum = 0;
    for(int i=0; i<5; ++i) {
        cin >> a;
        if(a>40) {
            sum += a;
        }
        else {
            sum += 40;
        }
    }
    cout << sum/5;
    getch();
    return 0;
}