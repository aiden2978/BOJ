#include <iostream>
using namespace std;

int main() {
    int n, d, m, y, birth, first=0, last=100000000;
    string name, old=" ", young=" ";
    cin >> n;

    for(int i=0; i<n; ++i) {
        cin >> name >> d >> m >> y;
        birth = d + m*100 + y*10000;
        if(birth>first) {
            first = birth;
            old = name;
        }
        if(birth < last) {
            last = birth;
            young = name;
        }
    }

    cout << old << endl << young << endl;
    system("pause");
    return 0;
}