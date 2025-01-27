#include <iostream>

using namespace std;

int main()
{
    int num = 0;
    cin >> num;

    switch(num){
    case 1:
        cout << "janeiro" << endl;
        break;
    case 2:
        cout << "fevereiro" << endl;
        break;
    case 3:
        cout << "marco" << endl;
        break;
    case 4:
        cout << "abril" << endl;
        break;
    case 5:
        cout << "maio" << endl;
        break;
    case 6:
        cout << "ju" << endl;
        break;
    case 7:
        cout << "jo" << endl;
        break;
    case 8:
        cout << "agosto" << endl;
        break;
    case 9:
        cout << "setembro" << endl;
        break;
    case 10:
        cout << "outubro" << endl;
        break;
    case 11:
        cout << "novembro" << endl;
        break;
    case 12:
        cout << "dezembro" << endl;
        break;
    default:
        cout << "invalido" << endl;
    }

    return 0;
}
