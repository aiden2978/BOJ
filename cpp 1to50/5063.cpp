#include <iostream>
using namespace std;

int main() {
    int T, r, e, c;
    cin >> T;
    for(int i=0;i<T;++i) {
        cin >> r >> e >> c;
        if(e>r+c) {
            cout << "advertise" << endl;
        }
        if(e==r+c) {
            cout << "does not matter" << endl;
        }
        if(e<r+c) {
            cout << "do not advertise" << endl;
        }
    }
    system("pause");
    return 0;
}