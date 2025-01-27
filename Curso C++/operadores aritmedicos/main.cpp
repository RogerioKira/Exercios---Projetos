#include <iostream>

using namespace std;

int main()
{
    int x,y;
    x = 3;
    y = 9;

    cout << "valor de x e y:" << x << ", " << y << endl;

    cout << "soma" << x + y << endl;
    cout << " subtracao" << x - y << endl;
    cout << " multiplicacao" << x * y << endl;
    cout << "divisao" << y / x << endl;

    double d = y/ (x + 1.0);
    cout << "divisao x e y :" << d << endl;

    system("pause");

    return 0;
}
