#include <iostream>
using namespace std;

int main() {
    int T, a, b;
    cin >> T;
    for(int cnt=0; cnt<T; ++cnt) {
        int yon=0, kor=0;
        for(int i=0; i<9; ++i) {
            cin >> a >> b;
            yon += a;
            kor += b;
        }
        if(yon>kor) {
            cout << "Yonsei" << endl;
        }
        if(yon<kor) {
            cout << "Korea" << endl;
        }
        if(yon==kor) {
            cout << "Draw" << endl;
        }
    }

    
    system("pause");
    return 0;
}