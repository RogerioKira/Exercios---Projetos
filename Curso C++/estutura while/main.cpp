#include <iostream>

using namespace std;

int main()
{
    int i = 0;
    do{
        i++;
        cout << "valor de i" << i << endl;
    }while(i<10);

    int i2 = 0;
    while(i>10){
        i++;
        cout << "valor de i2" << i2 << endl;
    }

    system("pause");
    return 0;
}
