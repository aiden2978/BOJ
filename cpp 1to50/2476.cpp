#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N, a, b, c, score, maxscore=0;
    cin >> N;
    for(int i=0; i<N; ++i) {
        cin >> a >> b >> c;
        if(a==b && a==c) {
            score = 10000 + a*1000;
        }
        else {
            if(a==b) {
                score = 1000 + a*100;
            }
            if(a==c) {
                score = 1000 + a*100;
            }
            if(b==c) {
                score = 1000 + b*100;
            }
            if(a!=b && a!=c && b!=c) {
                score = max({a, b, c})*100;
            }
        }
        if(score>maxscore) {
            maxscore = score;
        }
    }
    cout << maxscore << endl;
    system("pause");
    return 0;
}