#include <iostream>
using namespace std;

int main() {
    int n, p, c, cmax;
    string name, best;
    cin >> n;

    for(int i=0; i<n; ++i) {
        cin >> p;
        cmax = 0;
        best = " ";
        for(int j=0; j<p; ++j) {
            cin >> c >> name;
            if(c > cmax) {
                cmax = c;
                best = name;
            }
        }
        cout << best << endl;
    }

    system("pause");
    return 0;
}