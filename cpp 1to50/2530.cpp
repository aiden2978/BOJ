#include <iostream>
#include <conio.h>
using namespace std;

int main() {
    int h, m, s, t, tot;

    cin >> h >> m >> s;
    cin >> t;

    tot = (3600*h + 60*m + s + t) % 86400;

    s = tot % 60;
    m = (tot / 60) % 60;
    h = (tot / 60) / 60;

    printf("%d %d %d", h, m, s);
    getch();
    return 0;
}