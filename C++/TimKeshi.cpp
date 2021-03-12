/*
--------------------------------------------------
Name    : Tim Keshi
Author  : Danial Khorasanizadeh
Link    : quera.ir/problemset/contest/80651
Date    : 03/Mar/2021
--------------------------------------------------
*/
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int totalTeams = 0;
    int a, b;
    for (int i = 0; i < 3; i++)
    {
        cin >> a;
        cin >> b;
        totalTeams += min(a, b);
    }
    cout << totalTeams;
    return 0;
}