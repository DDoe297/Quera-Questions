/*
--------------------------------------------------
Name    : Brute Force Hello, World!
Author  : Danial Khorasanizadeh
Date    : 19/Mar/2021
--------------------------------------------------
*/
#include <iostream>
#include <ctime>
#include <thread>
#include <chrono>
using namespace std;
int random(int lower, int upper)
{
    int num = (rand() % (upper - lower + 1)) + lower;
    return num;
}
int main(void)
{
    string HelloWorld = "Hello, World!";
    srand(time(NULL));
    int i = 0;
    char randomChar;
    while (i < 13)
    {
        randomChar = random(32, 126);
        cout << randomChar;
        this_thread::sleep_for(chrono::milliseconds(10));
        if (randomChar == HelloWorld[i])
        {
            i++;
        }
        else
        {
            cout << "\b";
        }
    }
}