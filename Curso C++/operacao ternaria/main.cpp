#include <iostream>

using namespace std;

int main()
{
    cout << "digite numero" << endl;
    int i = 0;
    cin >> i;

    string texto;
    if(i<=10)
        texto = "menor que dez" ;
    else
        texto = "maior que dez";

    cout << "valor é " << texto << endl ;

    system ("pause");
    return 0;
}
