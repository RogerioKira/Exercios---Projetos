#include <iostream>

using namespace std;

int main()
{
    double val[5];
    for(int i = 0;i<=4; i++){
        cout << "informe " << i+1 <<"valor" << endl;
        cin >> val[i];
    }

    double total = 0;
    for(int i2 = 0; i2<=4; i2++){
        total = total + val[i2];
    }

    cout << std::fixed;
    cout << "media" << (total/5) << endl;

    return 0;
}
