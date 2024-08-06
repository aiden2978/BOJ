#include <iostream>
#include <algorithm>
#include <conio.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int num[3]{a, b, c};
    sort(num, num+3);
    cout << num[1];
    
    getch();
    return 0;
}