#include <iostream>

using namespace std;

int main()
{
    char c;
    cout << "digite ate g" << endl;
    cin >> c;

    switch(c){
    case 'a':
    case 'A':
        cout << "voce digitou a ou A "<< endl;
        break;
    case 'b':
    case 'B':
    case 'c':
    case 'd':
    case 'e':
    case 'f':
        cout << "entre b e f" << endl;
        break;
    default:
        cout << "ivalido" << endl;
    }

    system("pause");
    return 0;
}
