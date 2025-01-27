#include <iostream>

using namespace std;

int main()
{
    int num = 10;
    char c = 's';

    {
        cout<<"codigo" << endl;
        double din = 4.99;
        cout << "valor de dinheiro" << din << endl;
    }

    cout << "informe numero" << endl;
    cin >> num;
    if(num==50){
            cout << "bloco if" << endl;
    }else{
            cout << "bloco else" << endl;
    }

    system("pause");
    return 0;
}
