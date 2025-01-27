#include <iostream>

using namespace std;

int main()
{
    cout << "numero " << endl;
    int valor = 0;
    cin >> valor ;

    if(valor > 50){
        cout <<"maior que 50" << endl;
    }else{
        cout << "menor que 50" << endl;
    }

    system ("pause");
    return 0;
}
