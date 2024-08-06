#include <iostream>
using namespace std;

int main() {
    int N, a, b, q1=0, q2=0, q3=0, q4=0, axis=0;
    cin >> N;
    
    for(int i=0; i<N; ++i) {
        cin >> a >> b;
        if(a==0 || b==0) {
            axis += 1;
        }
        else {
            if(a>0 && b>0) {
                q1 += 1;
            }
            if(a<0 && b>0) {
                q2 += 1;
            }
            if(a<0 && b<0) {
                q3 += 1;
            }
            if(a>0 && b<0) {
                q4 += 1;
            }
        }
    }

    cout << "Q1: " << q1 << endl << "Q2: " << q2 << endl << "Q3: " << q3 << endl << "Q4: " << q4 << endl << "AXIS: " << axis << endl;
    
    system("pause");
    return 0;
}