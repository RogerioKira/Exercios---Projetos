#include <iostream>

using namespace std;

int main()
{
    int varInt = 100;
    char c = 'r';
    double pFlutuante = 5.99;

    cout << "o valor da variavel varInt e:"<<varInt<<endl;
    cout << "o valor da variavel c é" << c << endl;
    cout << "o valor da varivel pFlutuante" << pFlutuante << endl;

    cout << "memoria variavel varInt" <<sizeof(varInt) << endl;
    cout << "memoria de c" << sizeof(c) << endl;
    cout << "memoria de pFlutuante" << sizeof(pFlutuante) << endl;

    return 0;
}
