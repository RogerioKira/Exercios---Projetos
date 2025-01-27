#include <iostream>

using namespace std;

int main()
{
    double n1,n2,n3,n4;
    cout <<"primeira" << endl;
    cin >> n1;
    cout <<"segunda" << endl;
    cin >> n2;
    cout <<"terceira" << endl;
    cin >> n3;
    cout <<"quarta" << endl;
    cin >> n4;

    double soma  = n1+n2+n3+n4;
    soma = (soma/4);

    cout << "mdeia" << soma << endl << endl;

    if(soma >= 7){
        cout << "aprovado" << endl;
    }else{
        cout << "reprovado " << endl;
    }

    system("pause");
    return 0;
}
