#include <iostream>

using namespace std;

int main()
{
    int tabela[2][2];
    tabela[0][0]=10;
    tabela[0][1]=100;
    tabela[1][0]=20;
    tabela[1][1]=111;

    int t2 [2][2] = {
    {10,100},
    {20,111}
    };

    cout << "{{" << t2 [0][0] << "," << t2 [0][1] <<
                    t2 [1][0] << "," << t2 [1][1] << endl;

    return 0;
}
