#include <iostream>

using namespace std;

int main()
{
    cout << "numero para mes" << endl;

    int num = 0;
    cin >> num;

    string mes =(num==1)?"janeiro":
                (num==2)?"feve":
                (num==3)?"maco":
                (num==4)?"abriu":
                (num==5)?"maio":
                (num==6)?"ju":
                (num==7)?"jojo":
                (num==8)?"augusto":
                (num==9)?"ste":
                (num==10)?"out":
                (num==11)?"nove":
                (num==12)?"dezem":
                    "valor invalido";
        cout << mes << endl;

    system("pause");
    return 0;
}
