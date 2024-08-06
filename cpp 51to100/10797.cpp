#include <iostream>
using namespace std;

int main() {
    int n, a, b, c, d, e, cnt=0;
    cin >> n;
    cin >> a >> b >> c >> d >> e;
    if(a==n) {
        cnt += 1;
    }
    if(b==n) {
        cnt += 1;
    }
    if(c==n) {
        cnt += 1;
    }
    if(d==n) {
        cnt += 1;
    }
    if(e==n) {
        cnt += 1;
    }
    cout << cnt;
    system("pause");
    return 0;
}