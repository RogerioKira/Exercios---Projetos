#include <iostream>

using namespace std;

int main()
{
    int a = 5/2;
    int num1,num2;
    num1 = 10;
    num2 = 5;

    int div = num1 / num2;
    int resto = num1 % num2 ;

    cout <<"div" << div << endl;
    cout << "resto" << resto << endl;

    cout << "modulo de 3 e 2 " << 3 % 2 << endl;
    cout << "modulo de 4 e 2 " << 4 % 2 << endl;
    cout << "modulo de 5 e 2 " << 5 % 2 << endl;
    cout << "modulo de 6 e 2 " << 6 % 2 << endl;

    cout << 10 % 2 << endl;
    cout << 9 % 2 << endl;

    system ("pause");
    return 0;
}
