#include <iostream>
#include <conio.h>
using namespace std;

int main() {
    long long N, S;
    cin >> S;
    N = 0;
    while(1) {
        if((N+1)*(N+2)>2*S) {
            break;
        }
        else {
            N++;
        }
    }
    cout << N << endl;
    getch();
    return 0;
}