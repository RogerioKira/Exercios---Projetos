#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int num1,num2,soma,sub,multi,div;

    cout <<"calculadora"<< endl;
    cout <<"primeiro"<< endl;
    cin >> num1;
    cout << "segundo" << endl;
    cin >> num2;

    soma = num1 + num2;
    sub = num1 - num2;
    multi = num1 * num2;
    div = num1 / num2;

    cout <<"soma" << soma << endl;
    cout <<"subtracao" << sub << endl;
    cout <<"produto" << multi << endl;
    cout <<"divisao" << div << endl;

    system ("pause");
    return 0;
}
