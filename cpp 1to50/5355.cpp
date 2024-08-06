#include <iostream>
#include <conio.h>
#include <iomanip>
using namespace std;

int main() {
    int N;
    float n;
    char ch;

    cin >> N;

    for (int cnt = 0; cnt < N; ++cnt) {
        cin >> n;
        while(1) {
            // 일반적인 cin << ch는 공백을 무시하기 때문에 줄바꿈이 루프를 종료하도록 하려면 cin.get()를 사용
            cin.get(ch);
            if(ch == '\n'){
                break;
            }
            if(ch == '@'){
                n *= 3;
            }
            if(ch == '%'){
                n += 5;
            }
            if(ch == '#'){
                n -= 7;
            }
        }
        // fixed, setprecision을 통해 소수점 아래 자리수 고정
        cout << setprecision(2) << fixed;
        cout << n << endl;
    }
    
    getch();
    return 0;
}