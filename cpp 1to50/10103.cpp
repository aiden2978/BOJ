#include <iostream>
using namespace std;

int main() {
    int N, a, b, cy=100, sd=100;
    cin >> N;
    for(int i=0; i<N; ++i) {
        cin >> a >> b;
        if(a>b) {
            sd -= a;
        }
        if(a<b) {
            cy -= b;
        }
    }
    cout << cy << endl << sd << endl;
    system("pause");
    return 0;
}