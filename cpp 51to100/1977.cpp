#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b, from, to, sum = 0;
    cin >> a >> b;
    from = int(ceil(sqrt(a)));
    to = int(floor(sqrt(b)));

    if(from == to+1) {
        cout << -1 << endl;
    }
    else {
        for(int i=from;i<to+1;++i) {
            sum += i*i;
        }
        cout << sum << endl << from*from << endl;
    }

    system("pause");
    return 0;
}