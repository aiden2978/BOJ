#include <iostream>
using namespace std;

int main() {
    int N, i, sum;
    sum = 0;
    cin >> N;

    for(int cnt=0; cnt<N; ++cnt) {
        cin >> i;
        if(i==0) {
            sum -= 1;
        }
        else {
            sum += 1;
        }
    }

    if(sum > 0) {
        cout << "Junhee is cute!" << endl;
    }
    else {
        cout << "Junhee is not cute!" << endl;
    }

    system("pause");
    return 0;
}