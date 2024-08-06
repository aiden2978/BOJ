#include <iostream>
using namespace std;

int main() {
    int T, N, cons, max;
    string univ, yoar;
    cin >> T;

    for(int cnt=0; cnt<T; ++cnt) {
        cin >> N;
        yoar = " ";
        max = 0;
        for(int i=0; i<N; ++i) {
            cin >> univ >> cons;
            if(cons>max) {
                yoar = univ;
                max = cons;
            }
        }
        cout << yoar << endl;
    }
    
    system("pause");
    return 0;
}